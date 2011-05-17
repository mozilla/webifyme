var ANIMATE_TIME = 500;

$(document).ready(function() {
    
    attachLinkFunctions();

});
    
function attachLinkFunctions() {
    $("#gallery_container").fadeIn(ANIMATE_TIME);
    $("span.pages a").each(function() {
        $(this).unbind();
        $(this).click(function() {
            var href = $(this).attr('href');
            $("#gallery_container").fadeOut(ANIMATE_TIME, function() {
                $("#gallery_container").load(href, attachLinkFunctions);
            });
            $("span.pages .active").removeClass("active");
            $(this).addClass("active");
            return false;
        });
        
        function loadPage(href) {
            $("#gallery_container").load(href, attachLinkFunctions);
        }
    });
    
    $("a.gallery_nav").each(function() {
        $(this).unbind();
        $(this).click(function() {
            var href = $(this).attr('href') + "1/";
            
            $(".pagination").load($(this).attr('href'), attachLinkFunctions);
            $("#gallery_container").fadeOut(ANIMATE_TIME, function() {
                $("#gallery_container").load(href, attachLinkFunctions);
            });
            return false;
        });
    });
}