from django.contrib import admin
from application.models import PersonalInfo, MobileNumberInfo, TelephoneNumberInfo, SkillsInfo, CompanyInfo, CutOffPeriodInfo, AttendanceInfo,EmployeePayroll, EmployeeSalary, EmployeeLeaves, EmployeeItenerary,EmployeeIteneraryDetails,Concerns,Notifications
from import_export.admin import ImportExportModelAdmin 
# Register your models here.


admin.site.site_header = 'LITS System Super Administrator'
admin.site.index_title = 'LITS System Super Administrator Page'
admin.site.site_title = 'LITS System Super Administrator Panel'


class PersonalAdmin(ImportExportModelAdmin):
    list_display = ('id','fk_user',
                    'key_id',
                    'image',
                    'suffix',
                    'first_name',
                    'middle_name',
                    'last_name',
                    'dob',
                    'age',
                    'gender',
                    'address',
                    'date_started',
                    'date_added',
                    'education',
                    'experience',
                    'notes',
                    'emer_cont_pers',
                    'emer_cont_pers_cont_no',
                    )
    list_editable = ('image',
                     'suffix',
                     'first_name',
                     'middle_name',
                     'last_name',
                     'dob',
                     'age',
                     'gender',
                     'address',
                     'date_started',
                     'education',
                     'experience',
                     'notes',
                     'emer_cont_pers',
                     'emer_cont_pers_cont_no',)
    list_per_page = 10
    search_fields = ('suffix',
                     'first_name',
                     'middle_name',
                     'last_name',
                     'gender',
                     'address',
                     'date_started',
                     'education',
                     'experience',
                     'notes',
                     'emer_cont_pers',
                     'emer_cont_pers_cont_no',
                     )
    list_filter = ('dob',
                   'age',
                   'gender',
                   'date_started',)

admin.site.register(PersonalInfo, PersonalAdmin)

class MobileNumberAdmin(ImportExportModelAdmin):

    list_display = ('id','fk_mobile_user','mobile_number')
    list_editable = ('mobile_number',)
    list_per_page = 10
    search_fields = ('mobile_number',)
    list_filter = ('mobile_number',)

admin.site.register(MobileNumberInfo, MobileNumberAdmin)

class TelephoneNumberAdmin(ImportExportModelAdmin):

    list_display = ('id','fk_telephone_user','telephone_number')
    list_editable = ('telephone_number',)
    list_per_page = 10
    search_fields = ('telephone_number',)
    list_filter = ('telephone_number',)

admin.site.register(TelephoneNumberInfo, TelephoneNumberAdmin)


class SkillsAdmin(ImportExportModelAdmin):
        
    list_display = ('id', 'fk_skills_user', 'skills')
    list_editable = ('skills',)
    list_per_page = 10
    search_fields = ('skills',)
    list_filter = ('skills',)

admin.site.register(SkillsInfo, SkillsAdmin)

class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'fk_company_user', 'company_id', 'company_tin', 'designation','department', 'personal_tin', 'sss_number', 'pagibig', 'philhealth')
    list_editable = ('company_id', 'company_tin', 'designation','department', 'personal_tin', 'sss_number', 'pagibig', 'philhealth')
    list_per_page = 10
    search_fields = ('company_id', 'company_tin', 'designation','department', 'personal_tin', 'sss_number', 'pagibig', 'philhealth')
    list_filter = ('designation',)

admin.site.register(CompanyInfo, CompanyAdmin)


class CutOffPeriodAdmin(ImportExportModelAdmin):
    list_display = ("id","attendance_file","cut_off_period","date_created")
    list_editable = ("attendance_file",)
    list_per_page = 10
    search_fields = ("cut_off_period",)
    list_filter = ("cut_off_period",)


admin.site.register(CutOffPeriodInfo, CutOffPeriodAdmin)


class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ("id", "employee_profile", "cut_off_period", "days_of_week", "date", "time_in", "time_out", "late", "undertime","payment_computation_for_work_done" ,"overtime", "payment_computation_overtime","date_created")
    list_editable = ("employee_profile", "cut_off_period", "days_of_week", "date", "time_in", "time_out", "late", "undertime","payment_computation_for_work_done" , "overtime","payment_computation_overtime",)
    list_per_page = 15
    search_fields = ("days_of_week", "date", "time_in", "time_out", "late", "undertime", "payment_computation_for_work_done" , "overtime","payment_computation_overtime",)
    list_filter = ("employee_profile", "cut_off_period","payment_computation_for_work_done","payment_computation_overtime",)

admin.site.register(AttendanceInfo, AttendanceAdmin)

class EmployeePayrollAdmin(ImportExportModelAdmin):
    list_display = ('id', 'employee_fk','payroll_cutoff_period','payroll_date','monthly_rate','monthly_allowance','basic_pay','allowance','overtime_pay','legal_holiday','special_holiday','late_or_absences','salary_or_cash_advance','gross_pay','sss_premiums','philhealth_contribution','pagibig_contribution','withholding_tax','pagibig_loan','deducted_salary_cash_advance','total_deduction','net_pay','thirteenth_month_pay','date_added','is_seen')
    list_editable = ('employee_fk','payroll_cutoff_period','monthly_rate','monthly_allowance','basic_pay','allowance','overtime_pay','legal_holiday','special_holiday','late_or_absences','salary_or_cash_advance','gross_pay','sss_premiums','philhealth_contribution','pagibig_contribution','withholding_tax','pagibig_loan','deducted_salary_cash_advance','total_deduction','thirteenth_month_pay','net_pay','is_seen')
    list_per_page = 10
    search_fields = ('employee_fk','payroll_cutoff_period','payroll_date','monthly_rate','monthly_allowance','basic_pay','allowance','overtime_pay','legal_holiday','special_holiday','late_or_absences','salary_or_cash_advance','gross_pay','sss_premiums','philhealth_contribution','pagibig_contribution','withholding_tax','pagibig_loan','deducted_salary_cash_advance','total_deduction','thirteenth_month_pay','net_pay')
    list_filter = ('employee_fk','payroll_cutoff_period','payroll_date')

admin.site.register(EmployeePayroll, EmployeePayrollAdmin)


class EmployeeSalaryAdmin(ImportExportModelAdmin):
    list_display = ("id","employee_salary_fk","amount","allowance","date_added","reason")
    list_editable = ("employee_salary_fk","amount","allowance","reason")
    list_per_page = 10
    search_fields = ("id","employee_salary_fk","amount","allowance","date_added","reason")
    list_filter = ("date_added",)

admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)
 


#  list_display = ()
#  list_editable = ()
#  list_per_page = 10
#  search_fields = ()
#  list_filter = ()

class EmployeeLeavesAdmin(ImportExportModelAdmin):
    list_display = ('id','employee_leave_fk','date_filed', 'department','status','no_days','inclusive_dates','reasons','classification_of_leave','leave_credits','less_this_application','balance_as_of_this_date','noted_by','checked_by','approved_by',)
    list_editable = ('employee_leave_fk', 'department','status','no_days','inclusive_dates','reasons','classification_of_leave','leave_credits','less_this_application','balance_as_of_this_date','noted_by','checked_by','approved_by',)
    list_per_page = 10
    search_fields = ('id','employee_leave_fk','date_filed', 'department','classification_of_leave','noted_by','checked_by','approved_by', )
    list_filter = ('date_filed', 'department','classification_of_leave',)

admin.site.register(EmployeeLeaves, EmployeeLeavesAdmin)

class EmployeeIteneraryAdmin(ImportExportModelAdmin):    
    list_display = ('id','employee_itenerary_fk','date_filed','noted_by','checked_by','approved_by')
    list_editable = ('noted_by','checked_by','approved_by')
    list_per_page = 10
    search_fields = ('id','employee_itenerary_fk','date_filed','noted_by','checked_by','approved_by')
    list_filter = ('date_filed',)

admin.site.register(EmployeeItenerary, EmployeeIteneraryAdmin)

class EmployeeIteneraryDetailsAdmin(ImportExportModelAdmin):
    list_display = ('id','employee_itenerary','date','timeIn','timeOut','reasons')
    list_editable = ('date','timeIn','timeOut','reasons')
    list_per_page = 10
    search_fields = ('id','employee_itenerary','date','timeIn','timeOut','reasons')
    list_filter = ('date',)

admin.site.register(EmployeeIteneraryDetails, EmployeeIteneraryDetailsAdmin)

class ConcernsAdmin(ImportExportModelAdmin): 
    list_display = ('id','sender','receiver','subject','message','reply','date_filed',)
    list_editable = ('sender','receiver','subject','message','reply',)
    list_per_page = 10
    search_fields = ('id','sender','receiver','date_filed',)
    list_filter = ('sender','receiver','date_filed',)

admin.site.register(Concerns, ConcernsAdmin)

class NotificationsAdmin(ImportExportModelAdmin):
    list_display = ('id','sender','recipient','url','message','category','level','public','is_read','timestamp',)
    list_editable = ('sender','recipient','url','message','category','level','public','is_read',)
    list_per_page = 10
    search_fields = ('sender','recipient','url','message',)
    list_filter = ('category','level','public','is_read',)

admin.site.register(Notifications, NotificationsAdmin)



#  list_display = ()
#  list_editable = ()
#  list_per_page = 10
#  search_fields = ()
#  list_filter = ()

