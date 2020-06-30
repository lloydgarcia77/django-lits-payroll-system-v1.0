$(document).ready(function() {
    function calculate() {
        let basicPay = $("#basicPay").val() == "" ? 0 : $("#basicPay").val();
        let allowance = $("#allowance").val() == "" ? 0 : $("#allowance").val();
        let overtimePay = $("#overtimePay").val() == "" ? 0 : $("#overtimePay").val();
        let legalHoliday = $("#legalHoliday").val() == "" ? 0 : $("#legalHoliday").val();
        let sundaySpecialHoliday = $("#sundaySpecialHoliday").val() == "" ? 0 : $("#sundaySpecialHoliday").val();
        let lateAbsences = $("#basilateAbsencescPay").val() == "" ? 0 : $("#lateAbsences").val();
        let salaryCashAdvance = $("#salaryCashAdvance").val() == "" ? 0 : $("#salaryCashAdvance").val();
        //let grossPay = $("#grossPay").val() == null ? 0 : $("#grossPay").val();

        let philhealContribution = $("#philhealContribution").val() == "" ? 0 : $("#philhealContribution").val();
        let pagibigContribution = $("#pagibigContribution").val() == "" ? 0 : $("#pagibigContribution").val();
        let sssPremius = $("#sssPremius").val() == "" ? 0 : $("#sssPremius").val(); 

        let withholdingTax = $("#withholdingTax").val() == "" ? 0 : $("#withholdingTax").val();
        let pagibigLoan = $("#pagibigLoan").val() == "" ? 0 : $("#pagibigLoan").val();
        let deductionSalaryCashAdvance = $("#deductionSalaryCashAdvance").val() == "" ? 0 : $("#deductionSalaryCashAdvance").val();
        //let totalDeduction = $("#totalDeduction").val() == null ? 0 : $("#totalDeduction").val();

        let gp = parseFloat(basicPay) + parseFloat(allowance) + parseFloat(overtimePay) + parseFloat(legalHoliday) + parseFloat(sundaySpecialHoliday) + parseFloat(salaryCashAdvance);
        let td = parseFloat(lateAbsences) + parseFloat(philhealContribution) + parseFloat(pagibigContribution) + parseFloat(sssPremius) + parseFloat(withholdingTax) + parseFloat(pagibigLoan) + parseFloat(deductionSalaryCashAdvance);
        let np = gp - td;
        $("#grossPay").val(gp.toFixed(2));
        $("#totalDeduction").val(td.toFixed(2));
        $("#netPay").val(np.toFixed(2));
    }
    $("#basicPay, #allowance, #salaryCashAdvance, #overtimePay, #legalHoliday, #sssPremius, #sundaySpecialHoliday, #lateAbsences, #philhealContribution, #pagibigContribution, #withholdingTax, #pagibigLoan, #deductionSalaryCashAdvance").change(function() {
        calculate();
    });

    $("#btnDeletePayroll").on("click", function(e){
        e.preventDefault();
        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                
                $("#modal-default").modal("show");
            },
            success: function (data) { 
                $("#modal-default .modal-content").html(data.html_form);
            }
        });
        return false;
    });

    $("#modal-default").on("submit", ".frm-delete-payroll", function(e){
        e.preventDefault();
        let form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                // Note: The difference between href and replace, is that replace() removes the URL of 
                // the current document from the document history, meaning that it is not possible to 
                // use the "back" button to navigate back to the original document.
                if (data.form_is_valid) {
                    $("#modal-default").modal('hide'); 
                    window.location.replace(data.link);
                } else {
                    $("#modal-default .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


});