$(document).ready(function () { 
  
    let table = $('#tblCutOff').DataTable({
        'columnDefs': [ {
            //'targets': [1,2], /* column index */
            'targets': 3, /* column index */
            'orderable': false, /* true or false */ 
         }]
    });
    $("#btnUploadAttendance").on('click', function(e){
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

    
    $("#modal-default").on("submit", ".upload-attendance", function(e){
        e.preventDefault(); 

        let form = $(this);

        let formData = false;
        if (window.FormData){
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
            beforeSend: () =>{
                $("#modal-default .btnClose").attr("disabled", true);
                $("#btnSave span").text("Saving");
                $("#btnSave").removeClass("btn btn-primary ld-ext-right");
                $("#btnSave").addClass("btn btn-primary ld-ext-right running");
            },
            success: (data) => {
                if(data.success){
                    if (data.form_is_valid){
                        let list = data.list;
                        let id = list["id"];
                        let cut_off = list["cut_off"];
                        let date_created = list["date_created"];
                        let attendance_file_path = list["attendance_file_path"];
                        let url = list["url"];
                        
                        var myJSON = JSON.stringify(data.list,undefined, 4);
                        console.log(myJSON);
                        $("#modal-default").modal("hide"); 

                        table.row.add([
                            id,`<span class="label label-warning">${cut_off}</span>`,date_created,`
                            <div class="btn-group-vertical">
                            <button type="button" class="btn btn-block btn-danger btn-delete" data-toggle="tooltip"
                            title="Delete Attendance"  data-url="${url}">
                                <span class="fa fa-fw fa-trash"></span>
                                Delete</button>
                            <a href="${attendance_file_path}" class="btn btn-block btn-info" data-toggle="tooltip"
                            title="Download Attendance" download>
                                <span class="fa fa-fw fa-download"></span>
                                Download</a>
                            </div>


                            `
                            ]).draw(false);
                            
                    }else{
                        $("#modal-default .modal-content").html(data.html_form);
                        
                    }
                }else{
                    alert(data.success);
                    $("#modal-default .modal-content").html(data.html_form);
                    $("#modal-default .btnClose").text("Continue");
                    $("#btnSave").hide();
                }
                
            },
            complete: () => {
                $("#btnSave").removeClass("btn btn-primary ld-ext-right running");
                $("#btnSave").addClass("btn btn-primary ld-ext-right");
                $("#btnSave span").text("Save Changes");
                $("#modal-default .btnClose").attr("disabled", false);

            }
    
        });

      
        return false;
    });

    // $('button.btn-delete').on('click', function (e) {
    //     e.preventDefault();
    //     let row = $(this).closest("tr");
    //     console.log(row);
    //     table.row(row).remove().draw();
    //     return false;
    // });
    // very helpful
    //http://jsfiddle.net/s3dpj79q/ 
    $("#tblCutOff").on('click', ".btn-delete", function(e){
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

    

    $("#modal-default").on("submit",".delete-attendance", function(e){
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

        // $.ajax({
        //     url: form.attr("data-url"),
        //     data: form.serialize(),
        //     cache: false,
        //     type: form.attr("method"),
        //     dataType: 'json',
        //     success: (data) => {
        //         if(data.form_is_valid){  
        //             $("#modal-default").modal("hide"); 
        //             //table.clear().draw();
        //             //table.clear();
        //             table.destroy();
        //             table.clear();
        //             $("#tblCutOff tbody").html(data.table_records); 
        //             // Re initializing data table
        //             $('#tblCutOff').DataTable({
        //                 'columnDefs': [ {
        //                     //'targets': [1,2], /* column index */
        //                     'targets': 3, /* column index */
        //                     'orderable': false, /* true or false */ 
        //                  }]
        //             });
                    
        //             //table.columns.adjust().draw(); // Redraw the DataTable
        //         }else{
        //             $("#modal-form .modal-content").html(data.html_form);
        //         }
        //     }
        // });

        return false;
    });

});