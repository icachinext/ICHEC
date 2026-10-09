                (
                    function($) 
                    {
                        $.fn.visible = function(partial) 
                        {//拓展jQuery对象的方法
                            //alert("messageIn");
                            var $t = $(this),
                                $w = $(window),
                                viewTop = $w.scrollTop(),//视窗看到的顶部到网页顶部的距离
                                viewBottom = viewTop + $w.height(),//视窗看到的底部到网页顶部的距离
                                _top = $t.offset().top,//网页顶部的距离
                                _bottom = _top + $t.height(),//网页的底部到顶部的距离
                                //越往下值越大
                                compareTop = partial === true ? _bottom : _top,
                                compareBottom = partial === true ? _top : _bottom;
                                //当元素再可是窗口内部时
                            return ((compareBottom <= viewBottom) && (compareTop >= viewTop));

                        };

                    }
                )(jQuery);

    jQuery(document).ready
    (
        function($)
        {
            //执行到这一步
            var win = $(window);
            var allMods = $(".module");
            /*控制标签只显示一次*/
            allMods.each(function() {//对每一个有module class的元素进行函数操作
                var el = $(this);
                if (el.visible(true)) {
                    
                    el.addClass("come-in");
                }
                
            });

            win.scroll
            (
                function() 
                {

                allMods.each(function() {
                    var el = $(this);
                    if (el.visible(true)) {
                        el.addClass("come-in");
                    }
                    else{
                        el.removeClass("come-in");
                        el.removeClass("already-visible");
                    }
                });

                }
            )
        }
    );
  


