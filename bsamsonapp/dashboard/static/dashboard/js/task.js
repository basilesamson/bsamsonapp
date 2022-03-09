import { setUpPopups } from './popup.js';

$( document ).ready(function() {
    initTask();
});

function initTask() {
    setStepStatus();
    setDescription();
    addStep();
    
    // for each progress bar, do the updateProgressBar function
    $('span.progressBar').map(function() {
        updateProgressBar($(this), $(this).find('div.progressValue').attr('value'));
    });
}

function setDescription() {
    // set description textarea value to the description of the task
    if ($('.taskDescription').find('textarea').attr('task-description') != 'None') {
        $('.taskDescription').find('textarea').val($('.taskDescription').find('textarea').attr('task-description'));
    }

    $('.taskDescription').find('input').click(function() {
        if ($('.taskDescription').find('textarea').val() != '') {
            console.log($('.taskDescription').find('textarea').val());
            var formData = new FormData();
            var csrfTokenValue = $('.taskDescription').find('[name=csrfmiddlewaretoken]').val()
    
            // add values to formData
            formData.append('taskId', $('.taskDescription').find('textarea').attr('task-id'));
            formData.append('taskDescription', $('.taskDescription').find('textarea').val());
    
            const request = new Request('/task/set_description/', {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}});
    
            // send the request to the server
            fetch(request)
            .then(response => response.json())
            .then(result => {
                $('.taskDescription').find('textarea').blur();
            })
            .catch(error => {
                console.log(error)
            })
        }
    })

    // remove all \n of the description textarea
    $('.taskDescription').find('textarea').on('keyup', function(){ $(this).val($(this).val().replace(/[\r\n\v]+/g, '')); });

    // set text green when description textarea is focus
    $('.taskDescription').find('textarea').focus(() => { $('.taskDescription').find('form').find('div').css('color', '#06D7A0'); });
    $('.taskDescription').find('textarea').focusout(() => { $('.taskDescription').find('form').find('div').css('color', '#FFFFFF'); });

    // when enter is press in description textarea, simulate a click to send to the server
    $('.taskDescription').find('textarea').keypress(function(event) {
        if (event.keyCode == 13) {
            $('.taskDescription').find('input').click();
        }
    });
}

function addStep() {
    // this function add a step to a task on press enter and on click on add
    $('.addStep').find('i').click(function() { 
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
                        <b class="` + result['stepId'] + `">` + result['stepStatus'] + `</b>
                        <i class="fi fi-rr-angle-small-down task-status">
                            <div class="popup">
                                <span class="ajax-set-step-status">
                                    <i class="fi fi-sr-exclamation red"></i>
                                    <input id="` + result['stepId'] + `" data-url="/task/set_step_status/" type="submit" value="Bloqué">
                                </span>
                                <span class="ajax-set-step-status" >
                                    <i class="fi fi-sr-clock yellow"></i>
                                    <input id="` + result['stepId'] + `" data-url="/task/set_step_status/"type="submit" value="En cours">
                                </span>
                                <span class="ajax-set-step-status">
                                    <i class="fi fi-sr-checkbox green"></i>
                                    <input id="` + result['stepId'] + `" data-url="/task/set_step_status/" type="submit" value="Terminé">
                                </span>
                                <div class="separator"></div>
                                <span class="ajax-set-step-status">
                                    <input id="` + result['stepId'] + `" data-url="{% url 'task:setStepStatus' %}" type="submit" value="Supprimer">
                                </span>
                            </div>
                        </i>
                        <i icon="` + result['stepId'] + `" class="fi fi-rr-square"></i>
                        <i class="fi fi-rr-menu-dots"></i>
                    </span>
                </div>`);
                setUpPopups();
                initTask();
                $('.addStep').find('input[type=text]').val('');
                $('.addStep').find('input[type=text]').focus();
            })
            .catch(error => {
                console.log(error)
            })
        }
    });

    // when enter is press in addStep input text, simulate a click to send to the server
    $('.addStep').find('input[type=text]').keypress(function(event) {
        if (event.keyCode == 13) {
            $('.addStep').find('i').click();
        }
    });
    $('.addStep').find('form').submit(function (e) {
        e.preventDefault();
    });
}

function setStepStatus() {
    $('.ajax-set-step-status').click(
        function() {
            if ($(this).find('input').val() == "Supprimer") {
                // delete the step if input value clicked is Supprimer
                var formData = new FormData();

                // add values to formData
                formData.append('step', $(this).find('input').attr('id'));
    
                const request = new Request('/task/delete_step/', {method: 'POST', body: formData});
    
                // send the request to the server
                fetch(request)
                .then(response => response.json())
                .then(result => {
                    $('div#' + $(this).find('input').attr('id')).remove();
                    updateProgressBar($('span.progressBar'), result['progress']);
                })
                .catch(error => {
                    console.log(error)
                })
            } else {
                // set status to selected
                var formData = new FormData();

                // add values to formData
                formData.append('step', $(this).find('input').attr('id'));
                formData.append('status', $(this).find('input').val());
    
                const request = new Request('/task/set_step_status/', {method: 'POST', body: formData});
    
                // send the request to the server
                fetch(request)
                .then(response => response.json())
                .then(result => {
                    $('b.' + $(this).find('input').attr('id')).html(result['status']);
                    if (result['status'] == "Bloqué") {
                        $('[icon=' + $(this).find('input').attr('id') + ']').removeClass().addClass("fi fi-sr-exclamation red");
                    } else if (result['status'] == "Terminé") {
                        $('[icon=' + $(this).find('input').attr('id') + ']').removeClass().addClass("fi fi-sr-checkbox green");
                    } else {
                        $('[icon=' + $(this).find('input').attr('id') + ']').removeClass().addClass("fi fi-sr-clock yellow");
                    }
                    updateProgressBar($('span.progressBar'), result['progress']);
                })
                .catch(error => {
                    console.log(error)
                })
            }
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