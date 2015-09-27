$(document).ready(function() {
  $("#circle1").hide()
  $("#circle1").fadeIn(1000, 'swing');
  second();
  third();
  $('.indexcard').slick({
      accessibility: true
    });
});

$(".card").click(function() {
    $("#card").flip();
});
function second() {
  $("#arrow").css({opacity: 0});
  $("#arrow").delay(1000);
  $("#arrow").fadeTo(1000, 1, 'swing');
}

function third() {
  $("#circle2").css({opacity: 0});
  $("#circle2").delay(2000);
  $("#circle2").fadeTo(1000, 1, 'swing');
}
