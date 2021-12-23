$( document ).ready(function(){

$("#contactform").submit(function(e){
    e.preventDefault()
    var temp = $("#contactform").serialize();


    $.ajax({
        type:'POST',
        url: '/contact/',
        data: temp, 
        success: function (response) {
            
        }
    });

    this.reset();
    $(".form-part").remove();
    $(".feedback").html('Thank you for contacting us.');
});



$("#newsletter_form").submit(function(e){
    e.preventDefault()
    var temp = $("#newsletter_form").serialize();


    $.ajax({
        type:'POST',
        url: '/subscriptions/',
        data: temp, 
        success: function (response) {
            
        }
    });

    this.reset();
    $(".form-content").remove();
    var feedback = '<div class="subfeedback cta"><text>Thank you for subscribing !</text></div>'
    $("#subscription-part").append(feedback);
    
});














})