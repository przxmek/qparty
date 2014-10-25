//$(function() {
//    $("#playlist-btn").click(function() {
//        $("#mybox").animate({"left": "+=50px"}, "slow");
//    });
//});

$(document).ready(function(){
  $("#playlist-btn").click(function(){
    $(".wrapper").stop().animate({"left": "-1330px"}, "slow");
  });
});