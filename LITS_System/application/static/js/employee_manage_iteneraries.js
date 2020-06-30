$(document).ready(function () {
    let table =  $('#tblIteneraries').DataTable({
        'columnDefs': [ {
            'targets': 3, /* column index */
            'orderable': false, /* true or false */
        }]
    }); 
});