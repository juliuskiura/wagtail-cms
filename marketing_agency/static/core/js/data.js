$(document).ready(function () {
var fade = 1000
// This function removes the error highlighter when the user starts typing
$("#id_full_name").keyup(function () {
    $(this).removeClass('form-errors');    
    $(this).addClass('m-20');  
    $("#id_para_full_name").fadeOut(fade);
  });
$("#id_e_mail").keyup(function () {
    $(this).removeClass('form-errors');    
    $(this).addClass('m-20');  
    $("#id_para_e_mail").fadeOut(fade);
  });
$("#id_phone_number").keyup(function () {
    $(this).removeClass('form-errors');  
    $(this).addClass('m-20');  
    $("#id_para_phone_number").fadeOut(fade);
  });
$("#id_business").keyup(function () {
    $(this).removeClass('form-errors');    
    $(this).addClass('m-20');  
    $("#id_para_business").fadeOut(fade);
  });
$("#id_message").keyup(function () {
    $(this).removeClass('form-errors');  
    $(this).addClass('m-20');  
    $("#id_para_message").fadeOut(fade);
  });
//   application form. full name and phone number field have similar names to those in contact form so no need of extra code

 
$("#id_email").keyup(function () {
    $(this).removeClass('form-errors');    
    
    $("#id_para_email").fadeOut(fade);
  });

$("#id_about_yourself").keyup(function () {
    $(this).removeClass('form-errors');    
    
    $("#id_para_about_yourself").fadeOut(fade);
  });
$("#id_when_can_you_start").keyup(function () {
    $(this).removeClass('form-errors');  
    $("#id_para_when_can_you_start").fadeOut(fade);
  });
$("#id_monthly_salary_expectations").keyup(function () {
    $(this).removeClass('form-errors');  
    
    $("#id_para_monthly_salary_expectations").fadeOut(fade);
  });
$("#id_preferred_contract").keyup(function () {
    $(this).removeClass('form-errors');  
    
    $("#id_para_preferred_contract").fadeOut(fade);
  });
$("#id_consent").change(function () {
    $(this).removeClass('form-errors');  
    $(this).addClass('m-20');  
    $("#id_para_consent").fadeOut(fade);
  });
$("#id_document").change(function () {
    $(this).removeClass('form-errors');
    
    $("#id_para_document").fadeOut(fade);
  });


    function showErrors(d) {
        data = d;
                        
        var p = data;
            for (var key in p) {
            if (p.hasOwnProperty(key)) {
            var para_id = "id_para_" + key; 
            var field = "#id_" + key; 
            
            $(field).parent().append(`<div id="${para_id}" style="color: #721c24; background-color: #f8d7da; border-color: #f5c6cb; border: 1px solid transparent; border-top-color: transparent; border-radius: .25rem; margin-bottom:20px;">${p[key]}</div>`);
            $(field).addClass("form-errors");
            $(field).removeClass("m-20");
            $(field).focus();
            }
        }

        $(".systemerrors").append(
           `
            <div class="errors">            
                    <p class="errorin"><strong>Form failed to validate</strong></p>
                </div>
           
           `
        );
        $('.systemerrors').delay(10000).fadeOut(400);
    };

    $('.company-form').submit(function (e) {
        e.preventDefault();
        
        $("#id_para_full_name, #id_para_e_mail, #id_para_phone_number, #id_para_business, #id_para_message").remove()
        var temp = $(".company-form").serialize();       
        
        $.ajax({
            data: temp,
            type: $(this).attr("method"),
            url: '/contact/data-form',
            success: function (data) {
                if (data.form_saved) {
                        $(".form-part").delay(100).fadeOut(500);
                         $(".feedback").html(
                             ` 
                        <div class="form-success">
                    <p class=""><strong>${data.success}</strong></p>
                </div>                       
                       `
                             );
                } else{
                    
                    showErrors(data)

                }
            }
           
        });
        
    });

// JOBS

    $('.services-form').submit(function (e) {
        e.preventDefault();

        $("#id_para_jobpost,#id_para_jobtitle, #id_para_full_name, #id_para_email ,#id_para_phone_number, #id_para_about_yourself, #id_para_when_can_you_start, #id_para_monthly_salary_expectations, #id_para_preferred_contract, #id_para_consent, #id_para_document").remove()
        
        if ($('#id_consent').prop('checked') == false) {

            $('#id_consent').parent().append(`<div id="id_para_consent" style="color: #721c24; background-color: #f8d7da; border-color: #f5c6cb; border: 1px solid transparent; border-top-color: transparent; border-radius: .25rem;">Agree in checkbox is required</div>`);
            $('#id_consent').addClass("form-errors");
            $('#id_consent').focus();   


        } else { 
        
        $(this).ajaxSubmit({
         
            type: $(this).attr("method"),
            url: $(this).attr("action"),
            success: function (data) {
                if (data.form_saved) {
                        $(".form-part").delay(100).fadeOut(500);
                         $(".feedback").html(
                             ` 
                        <div class="form-success jobsuccess">
                    <p class=""><strong>${data.success}</strong></p>
                </div>                       
                       `
                             );
                } else{
                    
                    showErrors(data)

                }
            }
           
        });
    }
        
    });

})