
$( document ).ready(function() {
    initAccounts();
});

function initAccounts() {
    setDescription();
    setPicture();
}

function setPicture() {
    $('.set-user-picture').find('input[type=file]').change(function() {
        $('.set-user-picture').find('form').submit();
    });
    document.querySelector('i.set-user-picture').addEventListener('click', () => {
        document.querySelector('input[type=file]').click()
    })
}

function setDescription() {
    // set description textarea value to the description of the user
    if ($('.userDescription').find('textarea').attr('user-description') != 'None') {
        $('.userDescription').find('textarea').val($('.userDescription').find('textarea').attr('user-description'));
    }

    $('.userDescription').find('input').click(function() {
        var formData = new FormData();
        var csrfTokenValue = $('.userDescription').find('[name=csrfmiddlewaretoken]').val()

        // add values to formData
        formData.append('userId', $('.userDescription').find('textarea').attr('user-id'));
        formData.append('userDescription', $('.userDescription').find('textarea').val());

        const request = new Request('/accounts/profile/set_user_description/', {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}});

        // send the request to the server
        fetch(request)
        .then(response => response.json())
        .then(result => {
            $('.userDescription').find('textarea').blur();
            console.log(result['userProfileDescription']);
        })
        .catch(error => {
            console.log(error)
        })
    })

    // remove all \n of the description textarea
    $('.userDescription').find('textarea').on('keyup', function(){ $(this).val($(this).val().replace(/[\r\n\v]+/g, '')); });

    // set text green when description textarea is focus
    $('.userDescription').find('textarea').focus(() => { $('.userDescription').find('form').find('div').css('color', '#06D7A0'); });
    $('.userDescription').find('textarea').focusout(() => { $('.userDescription').find('form').find('div').css('color', '#FFFFFF'); });

    // when enter is press in description textarea, simulate a click to send to the server
    $('.userDescription').find('textarea').keypress(function(event) {
        if (event.keyCode == 13) {
            $('.userDescription').find('input').click();
        }
    });
}