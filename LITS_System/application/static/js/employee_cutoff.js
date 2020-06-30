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

//https://github.com/jdewit/bootstrap-timepicker/
//http://jdewit.github.io/bootstrap-timepicker/
//https://adminlte.io/themes/AdminLTE/documentation/index.html
// $('.timepicker').timepicker({
//     maxHours: 24,
//     showInputs: false,
//     showMeridian: false,
// })
    function calculateTime(index){
        // https://www.w3schools.com/jsref/jsref_sethours.asp
        if($(`#id_employee_personal_info_fk-${index}-time_in`).val() == "0:00" || $(`#id_employee_personal_info_fk-${index}-time_out`) == 0){
            $(`#id_employee_personal_info_fk-${index}-late`).val("");  
            $(`#id_employee_personal_info_fk-${index}-undertime`).val("");
            $(`#id_employee_personal_info_fk-${index}-overtime`).val("");
        }else{
            const starting_time = "08:30";
            const ending_time = "18:00";
            const grace_period = "08:45"
    
            let starting_time_hour = parseInt(starting_time.split(":")[0], 10);
            let starting_time_min = parseInt(starting_time.split(":")[1], 10);  
            
            let grace_period_hour = parseInt(grace_period.split(":")[0], 10);
            let grace_period_min = parseInt(grace_period.split(":")[1], 10);
    
            let ending_time_hour = parseInt(ending_time.split(":")[0], 10);
            let ending_time_min = parseInt(ending_time.split(":")[1], 10);
            
            //let time_in = $(`#id_employee_profile_fk-${index-1}-time_in`).val();
            let time_in = $(`#id_employee_personal_info_fk-${index}-time_in`).val();
         
            let time_out = $(`#id_employee_personal_info_fk-${index}-time_out`).val();    
              
    
            let time_in_hour = parseInt(time_in.split(":")[0], 10);
            let time_in_min = parseInt(time_in.split(":")[1], 10);
    
            let time_out_hour = time_out.split(":")[0];
            let time_out_min = time_out.split(":")[1];
    
            let late = "";
            let undertime = "";
            let overtime = "";
    
            // for late calculation
            const ti = new Date(); 
            ti.setHours(time_in_hour, time_in_min, 0, 0)
        
            const st = new Date();
            st.setHours(starting_time_hour,starting_time_min,0,0);
    
            const gp = new Date();
            gp.setHours(grace_period_hour, grace_period_min, 0, 0);
    
            if(ti.getTime() > gp.getTime()){ 
                let milliseconds = ti.getTime() - st.getTime();
                let seconds = milliseconds / 1000.0;
                let minutes = seconds / 60.0; 
                late = minutes;
            }
            // for under time calculation
    
            const to = new Date();
            to.setHours(time_out_hour, time_out_min, 0, 0);
    
            const et = new Date();
            //hour, min, sec, milli sec
            et.setHours(ending_time_hour, ending_time_min, 0, 0);
    
            if(to.getTime() < et.getTime()){
                let milliseconds = et.getTime() - to.getTime();
                let seconds = milliseconds / 1000.0;
                let minutes = seconds / 60.0;
                undertime = minutes;
            }else{
                if(time_out_hour > ending_time_hour){
                    overtime = time_out_hour - ending_time_hour; 
                }
            } 
            
            // $(`#id_employee_profile_fk-${index-1}-late`).val(late);  
            // $(`#id_employee_profile_fk-${index-1}-undertime`).val(undertime);
            // $(`#id_employee_profile_fk-${index-1}-overtime`).val(overtime); 
            $(`#id_employee_personal_info_fk-${index}-late`).val(late);  
            $(`#id_employee_personal_info_fk-${index}-undertime`).val(undertime);
            $(`#id_employee_personal_info_fk-${index}-overtime`).val(overtime);
        }
        
       
    }

    $('.timeIn').each(function(index){
     
        $(this).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(this).change(function(){  
            calculateTime(index);  
        });
    });

    $('.timeOut').each(function(index){
        $(this).timepicker({
            maxHours: 24,
            showInputs: false,
            showMeridian: false,
            defaultTime: "0:00",
        });

        $(this).change(function(){ 
            calculateTime(index); 
        });
    });
 


    $("#employee_attendance_cut_off_table").on("click", "#btnApplyChanges",function(e){
        e.preventDefault();
        $("#exclusive-modal-employee-cutoff").modal("show"); 
        return false;
    });

    $("#exclusive-modal-employee-cutoff").on("click", "#btnContinue" , function(e){
        e.preventDefault();
        $("#employee_attendance_cut_off_table").submit();
        //alert("Hwllo!");
        return false;
    }); 


 

});

