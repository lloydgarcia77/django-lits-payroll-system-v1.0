$(document).ready(function(e){
    let table = $('#tblEmployees').DataTable({
        'columnDefs': [{
            'targets': [1, 5], /* column index */
            'orderable': false, /* true or false */
        }]
    });

    $("#tblEmployees").on("click",".btn-delete", function(e){
        e.preventDefault();
        let url = $(this).attr("data-url");
        let row = $(this).closest('tr'); 
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
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

    $("#modal-default").on("submit",".delete-employee", function(e){
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
                }else{
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    $("#tblEmployeeList").on("click",".btn-payroll-settings", function(e){
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
    
    $("#modal-default").on("submit",".employee-payroll-settings-form",function(e){
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
                    location.reload();
                }else{
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

});