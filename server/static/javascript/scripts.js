//$(function() {
//    $("#playlist-btn").click(function() {
//        $("#mybox").animate({"left": "+=50px"}, "slow");
//    });
//});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

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
          $("#wrapper").removeClass('active-searchlist');
          $("#wrapper").addClass('active-playlist');
          inPlaylist = true
      }
  });
  $("#set-search-btn").click(function(){
      if (inPlaylist) {
          $("#wrapper").removeClass('active-playlist');
          $("#wrapper").addClass('active-searchlist');
          inPlaylist = false;
      }
  });
    $(".enqueue-btn").click(function(event) {
        var songID = $(this).attr('songid');
        var songName = $(this).attr('songname');
        $.post('/webparty/enqueue_song', {'songid': songID, 'songname': songName}, function() {
        });
    });
    setInterval(function () {
        getPlaylist();
    }, 1000);
    getPlaylist();
});
