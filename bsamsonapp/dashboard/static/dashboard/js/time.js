$(document).ready(function() {
    setInterval(setTime(), 1000);
    setInterval(setDate(), 1000);
});

function setDate() {
    var day = ['Dim.', 'Lun.', 'Mar.', 'Mer.', 'Jeu.', 'Ven.', 'Sam.'];
    var month = ['Jan', 'Fev', 'Mars', 'Avril', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Dec'];
    var today = new Date();

    $('h2#today').html(day[today.getDay()] + ' ' + today.getDate() + ' ' + month[today.getMonth()+1] + ' ' + today.getFullYear());
} 

function setTime() {
    var today = new Date()
    var hours = today.getHours()
    var minutes = today.getMinutes()

    if (hours < 10)
        hours = "0" + hours
    if (minutes < 10)
        minutes = "0" + minutes

    $('h1#time').html(hours + ":" + minutes);
}