# ICHEC / Chinese CHI

Jekyll 静态会议网站。`13/`–`20/` 保存历届网站归档；`21/` 之后的页面由 Jekyll 模板生成。根首页目前使用 2025 年内容，`27/` 为 2027 年会议页面。

## 构建与检查

使用 `.ruby-version` 指定的 Ruby 和 `Gemfile.lock` 锁定的依赖：

```sh
bundle install
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py _site
```

链接检查读取生成后的 HTML 和 CSS，检查本地文件、页面锚点及 `_redirects` 中的精确重定向。不联网验证外部链接，也不代替浏览器交互检查。`_site/` 是构建产物，不应直接编辑。

历届会议的历史日期、单位和投稿说明保留其当年的内容。归档缺件、资源恢复来源及本轮验证范围见 [工程检查记录](docs/site-audit-2026-10-29.md)。
