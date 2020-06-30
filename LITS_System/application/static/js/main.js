$(document).ready(function () {   
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

    $(".dropdown-menu li ul li a").on("click", function(e){
       // e.preventDefault();
        let url = $(this).attr("data-url");  
        //data or id is already retrievable on the url
        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: url, 
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    if(!(data.has_url)){
                        location.reload();
                    } 
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        }); 
        //return false;
    });
    
    $("#adminMarkAllNotifications").on("click",function(e){
        e.preventDefault();
        let url = $(this).attr("href");  
        //data or id is already retrievable on the url
        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: url, 
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    location.reload();
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        }); 
        return false;
    });

    const ShowNewProfileForm = function (e) {
        e.preventDefault();
        let url = $(this).attr("data-url");
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });

        return false;
    }

    const SaveProfileForm = function (e) {
        e.preventDefault();
        let form = $(this);
        let formData = false;

        if (window.FormData) {
            formData = new FormData(form[0]);
        }

        $.ajax({
            url: form.attr("data-url"),
            data: formData ? formData : form.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: () => {
            },
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-default").modal("hide");
                    location.reload();
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });

        return false;
    }

    $(".menuPersonal").on("click", ShowNewProfileForm);
    $("#modal-default").on("submit", ".new-profile-form", SaveProfileForm);


    $("#btnAddNewContact").on("click", function (e) {
        e.preventDefault();
        let url = $(this).attr("data-url");
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });


    $("#modal-default").on('submit', ".add-mobile-number-form", function (e) {
        e.preventDefault();
        let form = $(this);
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-default").modal('hide');
                    location.reload();
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


    $(".deleteMobileNo").on('click', function (e) {
        e.preventDefault();
        let url = $(this).attr("href");
        let id = url.substring(url.lastIndexOf("/") - 1, url.lastIndexOf("/"));



        let data = {
            "id": id
        }
        data = JSON.stringify(data);

        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: url,
            data: data, // json object to be transfer
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    location.reload();
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });

        return false;
    });

    // For Skills

    const ShowNewSkillForm = function (e) {
        e.preventDefault();
        let url = $(this).attr("data-url");

        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });

        return false;
    }


    $("#modal-default").on('submit', ".add-skill-form", function (e) {
        e.preventDefault();
        let form = $(this);
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-default").modal('hide');
                    location.reload();
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


    $("#addSkills").on("click", ShowNewSkillForm);

    $(".deleteSkills").on("click", function (e) {
        e.preventDefault();
        let url = $(this).attr("href");
        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: url,
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    location.reload();
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });
        return false;
    });

    // Company Details

    const ShowNewCompanyDetailsForm = function (e) {
        e.preventDefault();
        let url = $(this).attr("data-url");
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });

        return false;
    }

    const SaveNewCompanyDetailsForm = function (e) {
        e.preventDefault();
        let form = $(this);
        let formData = false;

        if (window.FormData) {
            formData = new FormData(form[0]);
        }

        $.ajax({
            url: form.attr("data-url"),
            data: formData ? formData : form.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: () => {
            },
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-default").modal("hide");
                    location.reload();
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });

        return false;
    }

    $(".menuCompany").on("click", ShowNewCompanyDetailsForm);
    $("#modal-default").on("submit", ".new-company-details-form", SaveNewCompanyDetailsForm);
    $("#modal-default").on("submit", ".edit-company-details-form", SaveNewCompanyDetailsForm);

    // Telephone Number

    $("#btnAddNewTelephoneNumber").on("click", function (e) {
        e.preventDefault();
        let url = $(this).attr("data-url");
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show");
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });

    $("#modal-default").on('submit', ".add-telephone-number-form", function (e) {
        e.preventDefault();
        let form = $(this);
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-default").modal('hide');
                    location.reload();
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    $(".deleteTelephoneNo").on('click', function (e) {
        e.preventDefault();
        let url = $(this).attr("href");  
        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: url, 
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    location.reload();
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }

        });

        return false;
    });

});
 
