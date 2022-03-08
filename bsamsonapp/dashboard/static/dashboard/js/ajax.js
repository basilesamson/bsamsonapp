import { setUpPopups } from './popup.js';

$( document ).ready(function() {
    setStepStatus();

    $('.addStep').find('input[type=text]').keypress(function(event) {
        if (event.keyCode == 13) {
            $('.addStep').find('i').click();
        }
    });
    $('.addStep').find('i').click(function() { addStep(); });
    

    // for each progress bar, do the updateProgressBar function
    $('span.progressBar').map(function() {
        updateProgressBar($(this), $(this).find('div.progressValue').attr('value'));
    })
});

function addStep() {
    if ($('.addStep').find('input[type=text]').val() != '') {
        var formData = new FormData();
        var csrfTokenValue = $('.addStep').find('[name=csrfmiddlewaretoken]').val()

        // add values to formData
        formData.append('stepName', $('.addStep').find('input[type=text]').val());
        formData.append('taskId', $('.addStep').find('input[type=text]').attr('task-id'));

        const request = new Request('/task/add_step/', {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}});

        // send the request to the server
        fetch(request)
        .then(response => response.json())
        .then(result => {
            $("div.list-item:last").before(`
            <div class="list-item">
                <span>` + result['stepName'] + `</span>
                <span>
                    <b id="` + result['stepId'] + `">` + result['stepStatus'] + `</b>
                    <i class="fi fi-rr-angle-small-down task-status">
                        <div class="popup">
                            <input id="` + result['stepId'] + `" data-url="/task/set_step_status/" class="ajax-set-step-status" type="submit" value="Bloqué">
                            <input id="` + result['stepId'] + `" data-url="/task/set_step_status/" class="ajax-set-step-status" type="submit" value="En cours">
                            <input id="` + result['stepId'] + `" data-url="/task/set_step_status/" class="ajax-set-step-status" type="submit" value="Terminé">
                        </div>
                    </i>
                    <i icon="` + result['stepId'] + `" class="fi fi-rr-square"></i>
                </span>
            </div>`);
            setUpPopups();
            updateProgressBar($('span.progressBar'), result['progress']);
            $('.addStep').find('input[type=text]').val('');
        })
        .catch(error => {
            console.log(error)
        })
    }
}

function setStepStatus() {
    $('.ajax-set-step-status').click(
        function() {
            var formData = new FormData();

            // add values to formData
            formData.append('step', $(this).attr('id'));
            formData.append('status', $(this).val());

            const request = new Request('/task/set_step_status/', {method: 'POST', body: formData});

            // send the request to the server
            fetch(request)
            .then(response => response.json())
            .then(result => {
                $('b#' + $(this).attr('id')).html(result['status']);
                if (result['status'] == "Bloqué") {
                    $('[icon=' + $(this).attr('id') + ']').removeClass().addClass("fi fi-sr-exclamation red");
                } else if (result['status'] == "Terminé") {
                    $('[icon=' + $(this).attr('id') + ']').removeClass().addClass("fi fi-sr-checkbox green");
                } else {
                    $('[icon=' + $(this).attr('id') + ']').removeClass().addClass("fi fi-sr-clock yellow");
                }
                updateProgressBar($('span.progressBar'), result['progress']);
            })
            .catch(error => {
                console.log(error)
            })
        }
    )
}

// this function update the progress bar given in parameter
function updateProgressBar(element, progress) {
    element.find('b').html(progress + '%');
    element.find($('div.progressValue')).css('width', progress + '%');
    if (progress == 100) {
        element.find($('div.progressValue')).css('background-color', '#06D7A0');
    } else {
        element.find($('div.progressValue')).css('background-color', '#0080FF');
    }
}