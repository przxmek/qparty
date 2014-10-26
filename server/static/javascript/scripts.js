function vote(url) {
    $.get(url, function(data) {
        $("#song_" + data[0] + "_votes").text(data[1]);
    });
}

function getPlaylist() {
    $.get("/player/playlist/votes/", function(data) {
        $("#playlist").html(data);

        $('.vote-btn').click(function(event) {
            vote($(this).attr('value'));
        });
    });
}

$(document).ready(function(){
    var inPlaylist = true;
  $("#set-playlist-btn").click(function(){
      if (!inPlaylist) {
          $(".content").animate({"left": "1%"}, "slow");
          inPlaylist = true
      }
  });
  $("#set-search-btn").click(function(){
      if (inPlaylist) {
          $(".content").animate({"left": "-97%"}, "slow");
          inPlaylist = false;
      }
  });
    setInterval(function () {
        getPlaylist();
    }, 1000);
    getPlaylist();
});