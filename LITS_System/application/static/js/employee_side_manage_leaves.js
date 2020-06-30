$(document).ready(function () {  
    let table =  $('#tblLeaves').DataTable({
        'columnDefs': [ {
            'targets': 6, /* column index */
            'orderable': false, /* true or false */
        }]
    });


    $("#tblLeaves").on('click', ".btn-delete", function(e){
        e.preventDefault();
        let url = $(this).attr("data-url");
        let row = $(this).closest('tr'); 
        //table.row(row).remove().draw(); 
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                //$("#modal-default").modal("show");
                $("#modal-default").data('tr',row).modal("show");
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

    $("#modal-default").on("submit",".delete-leave-form", function(e){
        e.preventDefault();
        let form = $(this); 
        let row = $("#modal-default").data('tr'); 
        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if(data.form_is_valid){  
                    $("#modal-default").modal("hide");
                    table.row(row).remove().draw();    
                }
                // else{
                //     $("#modal-form .modal-content").html(data.html_form);
                // }
            }
        });
 
        return false;
    });
});