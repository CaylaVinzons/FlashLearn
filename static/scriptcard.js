$(document).ready(function() {
  $('.indexcard').slick({
      accessibility: true
    });
});
$(".card").click(function() {
    $("#card").flip();
});