$( document ).ready(function() {
    $('.popup').css('display', 'none');
    popupUser();
});

function popupUser() {
    $('.user').hover(
        function() {
            $('section.user').find('.popup').css('display', 'flex');
        },
        function() {
            $('section.user').find('.popup').css('display', 'none');
        },
    )
}