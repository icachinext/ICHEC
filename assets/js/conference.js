$(function () {
  var $langToggle = $('[data-lang-toggle]');
  if ($langToggle.length) {
    var applyLang = function (lang) {
      document.documentElement.setAttribute('data-lang', lang);
      document.documentElement.lang = lang === 'zh' ? 'zh-Hans' : 'en';
      $langToggle.attr('aria-label', lang === 'zh' ? 'Switch to English' : '切换到中文');
    };
    var lang = document.documentElement.getAttribute('data-lang') === 'zh' ? 'zh' : 'en';
    applyLang(lang);
    $langToggle.on('click', function () {
      lang = lang === 'zh' ? 'en' : 'zh';
      try { localStorage.setItem('ichec27-lang', lang); } catch (e) {}
      applyLang(lang);
    });
  }

  new HSHeader($('#header')).init();

  new HSMegaMenu($('.js-mega-menu'), {
    desktop: {
      position: 'left'
    }
  }).init();

  AOS.init({
    duration: 650,
    once: true
  });

  $('.js-go-to').each(function () {
    new HSGoTo($(this)).init();
  });

  // Payment providers use separate mobile and desktop URLs.
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $('[data-device="mobile"]').prop('hidden', false);
    $('[data-device="desktop"]').prop('hidden', true);
  }

  // Fixed section menu on the call-for-papers pages: stays below the hero
  // and highlights the section currently scrolled into view.
  var $siderMenu = $('#sider-menu');
  if ($siderMenu.length) {
    var heroBottom = 810;
    var $items = $siderMenu.find('.navbar-nav > li');
    var $sections = $('.blockList');

    $(window).on('scroll', function () {
      var scrollTop = $(window).scrollTop();
      var current = 0;

      $siderMenu.css('top', Math.max(20, heroBottom - scrollTop));
      $sections.each(function (i) {
        if (scrollTop >= $(this).offset().top) {
          current = i;
        }
      });
      $items.removeClass('active').eq(current).addClass('active');
    }).trigger('scroll');
  }
});
