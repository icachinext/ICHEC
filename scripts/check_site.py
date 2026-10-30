#!/usr/bin/env python3
"""Check a Jekyll build's local links, fragments and CSS dependencies.

Usage: python3 scripts/check_site.py [_site]
External URLs are deliberately not treated as verified by this offline check.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit

CSS_URL = re.compile(r"url\(\s*['\"]?([^)'\"\s]+)", re.I)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.ids = set()
        self.links = []
        self.style = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src', 'poster', 'action', 'data-src'):
            if attrs.get(key):
                self.links.append((attrs[key], self.getpos()[0], key == 'href'))
        for url in CSS_URL.findall(attrs.get('style', '')):
            self.links.append((url, self.getpos()[0], False))
        self.style = tag == 'style' or self.style

    def handle_endtag(self, tag):
        if tag == 'style':
            self.style = False

    def handle_data(self, data):
        if self.style:
            self.links.extend((url, self.getpos()[0], False) for url in CSS_URL.findall(data))

    def handle_comment(self, data):
        # Legacy archives still load assets through IE conditional comments.
        conditional = re.fullmatch(r'\[if\b[^]]*\]>(.*?)<!\[endif\]', data.strip(), re.S)
        if conditional:
            nested = Page(self.source)
            nested.feed(conditional.group(1))
            self.ids.update(nested.ids)
            self.links.extend((url, self.getpos()[0] + line - 1, fragment)
                              for url, line, fragment in nested.links)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', nargs='?', default='_site', type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    if not (root / 'index.html').is_file():
        parser.error(f'{root} is not a built site (index.html missing)')
    pages = {}
    for path in sorted(root.rglob('*.html')):
        if not path.is_file():
            continue
        page = Page(path)
        page.feed(path.read_text(encoding='utf-8'))
        pages[path] = page
    redirects = {}
    redirect_file = root / '_redirects'
    if redirect_file.exists():
        for line in redirect_file.read_text().splitlines():
            fields = line.split()
            if len(fields) == 3 and not line.startswith('#'):
                redirects[fields[0]] = fields[1]
    errors = set()
    external = set()

    def check(source, url, line, fragment):
        base = '/' + source.relative_to(root).as_posix()
        if base.endswith('/index.html'):
            base = base[:-10]
        parsed = urlsplit(urljoin(base, url.strip()))
        if parsed.scheme or parsed.netloc:
            if parsed.scheme in ('http', 'https'):
                external.add(url)
            return
        target = parsed.path
        seen = set()
        while target in redirects:
            if target in seen:
                errors.add((str(source.relative_to(root)), line, 'redirect cycle', url))
                return
            seen.add(target)
            target = redirects[target]
        path = root / unquote(target).lstrip('/')
        if path.is_dir():
            path /= 'index.html'
        if not path.is_file() and not path.suffix:
            path = path.with_suffix('.html')
        if not path.is_file():
            errors.add((str(source.relative_to(root)), line, 'missing file', url))
        elif fragment and parsed.fragment and path in pages:
            anchor = unquote(parsed.fragment)
            if anchor not in pages[path].ids and not anchor.startswith(':~:text='):
                errors.add((str(source.relative_to(root)), line, 'missing anchor', url))

    for path, page in pages.items():
        for url, line, fragment in page.links:
            check(path, url, line, fragment)
    for path in sorted(root.rglob('*.css')):
        if not path.is_file():
            continue
        content = path.read_text(encoding='utf-8')
        for match in CSS_URL.finditer(content):
            check(path, match.group(1), content.count('\n', 0, match.start()) + 1, False)
    for source, line, kind, url in sorted(errors):
        print(f'{source}:{line}: {kind}: {url}')
    counts = Counter(error[2] for error in errors)
    print(f'Checked {len(pages)} HTML pages; {len(errors)} errors {dict(counts)}; '
          f'{len(external)} external URLs not checked.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
