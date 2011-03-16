$(document).ready(function() {
    $("a.download-reminder").click(function() {
	if(!$("#download_popup").hasClass("clicked")) {
	    $("#download_popup").center().fadeIn().addClass("clicked");
	    return false;
	}
    });

    $('body').click(function() {
	if($("#download_popup").hasClass("clicked")) {
	    $("#download_popup").fadeOut();
	    $("#download_popup").removeClass("clicked");
	}
    });

    $('#download_popup').click(function(event){
	event.stopPropagation();
    });

});

jQuery.fn.center = function () {
    this.css("position","absolute");
    this.css("top", ( $(window).height() - this.height() ) / 2+$(window).scrollTop() + "px");
    this.css("left", ( $(window).width() - this.width() ) / 2+$(window).scrollLeft() + "px");
    return this;
}