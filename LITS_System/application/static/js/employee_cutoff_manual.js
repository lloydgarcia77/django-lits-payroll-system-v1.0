$(document).ready(function () {
    //https://bootstrap-datepicker.readthedocs.io/en/latest/
    let days_of_week = [
        "SUN",
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT" 
    ]
    // $('#datepicker').datepicker({
    //     format: "dd",
    //     autoclose: true,
    //     enableOnReadonly: false,
    //     clearBtn: true,
    //     disableTouchKeyboard: true,
    //   }).on(`changeDate`, function(e) {
    //     // `e` here contains the extra attributes
        
    //     //let date = Date.parse(e.date);
    //     let date = new Date(e.date);
    //     console.log(days_of_week[date.getDay()]);
    //     alert(date.getDay());
    // });

    $(".mydate").each(function(index){
        $(this).datepicker({
            format: "dd",
            autoclose: true,
            //enableOnReadonly: false,
            clearBtn: true,
            //disableTouchKeyboard: true,
          }).on(`changeDate`, function(e) {
            // `e` here contains the extra attributes
            let date = new Date(e.date);
            $(`#id_cut_off_period_fk-${index}-days_of_week`).val(days_of_week[date.getDay()]);
        });
    });

    function calculateTime(index){

        // https://www.w3schools.com/jsref/jsref_sethours.asp
        if ($(`#id_cut_off_period_fk-${index}-time_in`).val() == "0:00" || $(`#id_cut_off_period_fk-${index}-time_out`).val() == "0:00"){
            $(`#id_cut_off_period_fk-${index}-late`).val(""); 
            $(`#id_cut_off_period_fk-${index}-undertime`).val("");
            $(`#id_cut_off_period_fk-${index}-overtime`).val("");
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
            let time_in = $(`#id_cut_off_period_fk-${index}-time_in`).val(); 
            let time_out = $(`#id_cut_off_period_fk-${index}-time_out`).val();    
              
    
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
            $(`#id_cut_off_period_fk-${index}-late`).val(late); 
            $(`#id_cut_off_period_fk-${index}-undertime`).val(undertime);
            $(`#id_cut_off_period_fk-${index}-overtime`).val(overtime);
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
             if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(index);
            }
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
             if($(this).val() == "0:00"){
                $(this).val("");
            }else{
                calculateTime(index);
            }
        });
    });

    $("#employee_attendance_cut_off_manual_table").on("click", "#btnApplyChangesManual",function(e){
        e.preventDefault();
        $("#exclusive-modal-employee-cutoff-manual").modal("show"); 
        return false;
    });

    $("#exclusive-modal-employee-cutoff-manual").on("click", "#btnContinue" , function(e){
        e.preventDefault();
        $("#employee_attendance_cut_off_manual_table").submit();
        //alert("Hwllo!");
        return false;
    }); 

 

});

