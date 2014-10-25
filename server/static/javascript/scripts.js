//$(function() {
//    $("#playlist-btn").click(function() {
//        $("#mybox").animate({"left": "+=50px"}, "slow");
//    });
//});

$(document).ready(function(){
    var inPlaylist = true;
  $("#set-playlist-btn").click(function(){
      if (inPlaylist) {
          $(".content").animate({"left": "-97%"}, "slow");
          inPlaylist = false
      }
  });
  $("#set-search-btn").click(function(){
      if (!inPlaylist) {
          $(".content").animate({"left": "1%"}, "slow");
          inPlaylist = true;
      }
  });
});