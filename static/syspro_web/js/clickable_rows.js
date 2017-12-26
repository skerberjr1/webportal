$(document).ajaxStop(function() {
    Init();
});
$(document).ready(function($) {
    Init();
});

function Init() {
    $('.clickable-row').click(function(event) {
        data = $(this).children(':first').text();
        data_type = $(this).closest('table').attr('data-type');
        window.location = '/syspro_web/' + data_type + '/' + data
    });
    $('.clickable-row').hover(function() {
            $(this).css('background-color', '#ccc');
        }, function() {
            $(this).css('background-color', '');
    });
}