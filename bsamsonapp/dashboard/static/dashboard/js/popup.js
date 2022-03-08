$( document ).ready(function() {
    setUpPopups();
});

export function setUpPopups() {
    // set all popup display to none
    $('.popup').css('display', 'none');

    // for each popup, get his parent and set hover = display to flex
    $('.popup').map(function() {
        $(this).parent().hover(
            function() {
                $(this).find('.popup').css('display', 'flex');
            },
            function() {
                $(this).find('.popup').css('display', 'none');
            },
        )
    })
}