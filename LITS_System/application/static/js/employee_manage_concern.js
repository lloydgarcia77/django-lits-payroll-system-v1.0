$(document).ready(function () {    
    let table =  $('#tblAdminConcerns').DataTable({
        'columnDefs': [ {
            'targets': 3, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 


    $("#newAdminConcern").on("click", function(e){
        e.preventDefault();
        let url = $(this).attr("href");
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show"); 
                
            },
            success: (data) => {
                $("#modal-default .modal-content").html(data.html_form);
                $('#modal-default #concernTo').select2();
            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });

    $("#modal-default").on("submit", ".create-admin-concern-form", function(e){
        e.preventDefault();
        let form = $(this);

        $.ajax({
            url:  form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: () => {
                $("#modal-default").modal("show"); 
                
            },
            success: (data) => {
                if(data.form_is_valid){
                    let concern_date_dict = data.concern_date_dict;
                    let id  = concern_date_dict["id"];
                    let subject  = concern_date_dict["subject"];
                    let date_filed  = concern_date_dict["date_filed"];
                    let edit_url  = concern_date_dict["edit_url"];
                    let delete_url  = concern_date_dict["delete_url"];
                    let view_url  = concern_date_dict["view_url"];
                    let myJSON = JSON.stringify(concern_date_dict,undefined, 4); 
                    $("#modal-default").modal('hide');
                    table.row.add([
                        `<span class="badge bg-red">${id}</span> `,
                        `<span class="label label-info">${subject}</span>`,
                        `<span class="label label-default">${date_filed}</span> `,
                        `
                        <div class="text-center"> 
                        <div class="btn-group">
                        <button type="button" class="btn btn-danger btn-delete" data-toggle="tooltip" title="Delete" data-url="${delete_url}"><i class="fa fa-fw fa-trash"></i></button>                    
                        <button type="button" class="btn btn-warning btn-view" data-toggle="tooltip" title="View" data-url="${view_url}"><i class="fa fa-fw fa-eye"></i></button>
                        <button type="button" class="btn btn-info btn-edit" data-toggle="tooltip" title="Edit" data-url="${edit_url}"><i class="fa fa-fw fa-pencil-square-o"></i></button>
                        </div>
                        </div>
                        `
                    ]).draw(false);
                }else{
                    $("#modal-default .modal-content").html(data.html_form);
                }

            },
            complete: (data) => {

            },
            error: (data) => {

            }
        });
        return false;
    });

    $("#tblAdminConcerns").on('click', ".btn-edit", function(e){
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

    $("#modal-default").on("submit",".edit-admin-concern-form", function(e){
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
                    let concern_date_dict = data.concern_date_dict; 
                    let subject  = concern_date_dict["subject"]; 
                    let edit_url  = concern_date_dict["edit_url"];
                    let delete_url  = concern_date_dict["delete_url"];
                    let view_url  = concern_date_dict["view_url"];
                    $("#modal-default").modal("hide");
                    var row_data = table.row(row).data();
                    row_data[1] = `<span class="label label-info">${subject}</span>`;
                    //https://legacy.datatables.net/ref
                    $('#tblAdminConcerns').dataTable().fnUpdate(row_data,row,undefined,false);
                    //alert(row_data[2]);
                }else{
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    });

    $("#tblAdminConcerns").on('click', ".btn-view", function(e){
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

    $("#tblAdminConcerns").on('click', ".btn-delete", function(e){
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
    $("#modal-default").on("submit",".delete-admin-concern-form", function(e){
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
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

   
});