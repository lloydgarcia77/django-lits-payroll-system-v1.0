
$(document).ready(function () {   
    $('.frmEIDDate').datepicker({ 
            autoclose: true,
        }).datepicker("setDate",'now');
    initialize_widgets();
    function initialize_widgets(){
        // $('.frmEIDDate').datepicker({ 
        //     autoclose: true,
        // }).datepicker("setDate",'now');
    
        $(".frmEIDTimeIn, .frmEIDTimeOut").timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });
        $("#formEIDOuter .ifReasons").prop("required", true);
    }
    
    $("#add_field_forEID").click(function(e){
        e.preventDefault(); 
        //get the total forms
        let form_idx = $("#formEIDOuter #id_employee_itenerary-TOTAL_FORMS").val();
        //when edit mode or with query is enable initial form is set upon edit and deleting
        let form_idx_init = $("#formEIDOuter #id_employee_itenerary-INITIAL_FORMS").val();

        $("#formEIDOuter").append($("#empty_frmEID").html().replace(/__prefix__/g, form_idx));
        $(`#id_employee_itenerary-${form_idx}-date`).datepicker({  
            autoclose: true,
        }).datepicker("setDate",'now');
        initialize_widgets();
        $("#formEIDOuter #id_employee_itenerary-TOTAL_FORMS").val(parseInt(form_idx) + 1);
        
        if(form_idx > 0){
            $("#del_field_forEID").show();
        }else{
            $("#del_field_forEID").hide();
        }
    
        return false;
    });

    $("#del_field_forEID").click(function(e){
        e.preventDefault();
        let form_idx = $("#formEIDOuter #id_employee_itenerary-TOTAL_FORMS").val();
        $('#formEIDOuter .fromEIDInner').last().remove();
        $("#formEIDOuter #id_employee_itenerary-TOTAL_FORMS").val(parseInt(form_idx)-1);
        let form_idx_after = $("#formEIDOuter #id_employee_itenerary-TOTAL_FORMS").val(); 
        
        if(form_idx_after <= 1){
            $("#del_field_forEID").hide();
        }
        return false;
    });

    
    
    
});

