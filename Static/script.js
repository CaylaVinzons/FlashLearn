$(document).ready(function() {
  $("#circle1").hide()
  $("#circle1").fadeIn(700, 'swing');
  second();
  third();
  $('.indexcard').slick({
      accessibility: true
    });
});

$("#card1").click(function() {
    $("#card1").flip('toggle');
});
function second() {
  $("#arrow").css({opacity: 0});
  $("#arrow").delay(400);
  $("#arrow").fadeTo(700, 1, 'swing');
}

function third() {
  $("#circle2").css({opacity: 0});
  $("#circle2").delay(1000);
  $("#circle2").fadeTo(700, 1, 'swing');
}
