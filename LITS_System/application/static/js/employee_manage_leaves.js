$(document).ready(function () {  
    let table =  $('#tblLeaves').DataTable({
        'columnDefs': [ {
            'targets': 7, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 
});