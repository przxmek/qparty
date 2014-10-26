function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        width: '800',
        height: '485',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function playNextSong() {
    $.getJSON('/player/next_song/', function(data) {
        player.loadVideoById(data);
    });
}

function popSong() {
    $.get('/player/pop_song/', function() {
        getPlaylist();
        playNextSong();
    });
}

function onPlayerReady(event) {
    $('#player').addClass('player')
    playNextSong();
}

function onPlayerStateChange(event) {
    if (event.data == 0) {
        popSong();
    }
}

function getPlaylist() {
    $.get("/player/playlist/", function(data) {
        $("#playlist-container").html(data);
    });
}

$(document).ready(function() {
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    getPlaylist();
    setInterval(function () {
        getPlaylist();
    }, 2000);

});