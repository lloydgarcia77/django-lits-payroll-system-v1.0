$(document).ready(function () {   
    
    let table =  $('#tblAdminInboxConcerns').DataTable({
        'columnDefs': [ {
            'targets': 3, /* column index */
            'orderable': false, /* true or false */
        }]
    });  

    $("#tblAdminInboxConcerns").on('click', ".btn-reply", function(e){
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


    $("#modal-default").on("submit",".reply-concern-form", function(e){
        e.preventDefault();
        let form = $(this);  
        
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {  
                if(data.form_is_valid){  
                    $("#modal-default").modal("hide");  
                }else{
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
});