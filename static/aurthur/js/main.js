// :: Typed js
var typed = new Typed('#typed', {
  stringsElement: '#typed-strings',
  typeSpeed: 50,
  backDelay: 1500,
  loop: 1,
  startDelay: 1000
}); // jQuery for page scrolling feature - requires jQuery Easing plugin

$(function () {
  $('.page-scroll').bind('click', function (event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
  });
}); // Highlight the top nav as scrolling occurs

$('body').scrollspy({
  target: '.fixed-top'
}); // Closes the Responsive Menu on Menu Item Click

$('.navbar-collapse ul li a').click(function () {
  $('.navbar-toggle:visible').click();
});