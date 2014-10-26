$(document).ready(function ($) {
    if (window.location.href.match(/.*\/#join-modal/))
        $('#join-modal').modal()
    else if (window.location.href.match(/.*\/#host-modal/))
        $('#host-modal').modal()
});