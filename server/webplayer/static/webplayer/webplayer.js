function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        width: '800',
        height: '485',
        videoId: 'zJLGc1XCeq8',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

function onPlayerStateChange(event) {
    if (event.data == 0) {
        $.getJSON('/player/next_song/', function(data) {
            event.target.loadVideoById(data);
        });
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
    }, 3000);
});