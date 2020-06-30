from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import os
# Create your models here.

def file_validator(value):

    file_size = value.size
    valid_file_extension = ['.xlsx','.xls']

    file_extension = os.path.splitext(value.name)[1]

    print("File Name: ", value.name)
    print("File Extension: ", file_extension)

    file_size_kb = file_size * 0.001
    file_size_mb = file_size_kb * 0.0001

    print("File Size: ", file_size, " Bytes")
    print("File Size: ", file_size_kb, " KB")
    print("File Size: ", file_size_mb, " MB")

    if not file_extension in valid_file_extension:
        print("Invalid file! Valid files only: ('.xlsx', '.xls')")
        raise ValidationError("Invalid file! Valid files only: ('.xlsx', '.xls')")

    else:
        if file_size_mb > 5: # 5MB
            print("File too large! The maximum file size can be upload is 5 MB")
            raise ValidationError("The maximum file size can be upload is 5 MB")
        else:
            print('FILE is VALID')
            return value

def file_validator_image(value):

    file_size = value.size
    valid_file_extension = ['.jpg', '.png', '.jpeg', '.pdf', '.doc', '.docx']

    file_extension = os.path.splitext(value.name)[1]

    print("File Name: ", value.name)
    print("File Extension: ", file_extension)

    file_size_kb = file_size * 0.001
    file_size_mb = file_size_kb * 0.0001

    print("File Size: ", file_size, " Bytes")
    print("File Size: ", file_size_kb, " KB")
    print("File Size: ", file_size_mb, " MB")

    if not file_extension in valid_file_extension:
        print("Invalid file! Valid files only: ('.jpg', '.png', '.jpeg', 'pdf', 'doc', 'docx')")
        raise ValidationError("Invalid file! Valid files only: ('.jpg', '.png', '.jpeg', 'pdf', 'doc', 'docx')")

    else:
        if file_size_mb > 5: # 5MB
            print("File too large! The maximum file size can be upload is 5 MB")
            raise ValidationError("The maximum file size can be upload is 5 MB")
        else:
            print('FILE is VALID')
            return value

class PersonalInfo(models.Model):
    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_to_user')
    key_id =  models.CharField(max_length=255,unique=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, validators=[file_validator_image])
    suffix = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    dob = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_LIST, default='Male')
    address = models.CharField(max_length=255, blank=True, null=True)
    date_started = models.DateField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    education = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)

    emer_cont_pers = models.CharField(max_length=50, blank=True, null=True)
    emer_cont_pers_cont_no = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.last_name + " " + self.first_name + " " + self.middle_name)

    # mobile
    # telephone
    # skills

class MobileNumberInfo(models.Model):
    fk_mobile_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mobile_to_user')
    mobile_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.mobile_number)

class TelephoneNumberInfo(models.Model):
    fk_telephone_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telephone_to_user')
    telephone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.telephone_number)

class SkillsInfo(models.Model):
    fk_skills_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills_to_user')
    skills = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.skills)

class CompanyInfo(models.Model):
    fk_company_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_to_user')
    company_id = models.CharField(max_length=50, blank=True, null=True)
    company_tin = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    personal_tin = models.CharField(max_length=50, blank=True, null=True)
    sss_number = models.CharField(max_length=50, blank=True, null=True)
    pagibig = models.CharField(max_length=50, blank=True, null=True)
    philhealth = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.company_id)

class CutOffPeriodInfo(models.Model):
    # cut_off_period_fk = models.OneToOneField(ProfileInfo, on_delete=models.CASCADE, related_name="cut_off_period_fk")
    attendance_file = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name="Attendance .xlsx file")
    cut_off_period = models.CharField(max_length=100, unique=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cut_off_period

Computing_Pay_for_Work_Done  = (
    ('Regular Day','Regular Day'),
    ('Special Day','Special Day'),
    ('Special Day and Rest Day','Special Day and Rest Day'),
    ('Regular Holiday','Regular Holiday'),
    ('Regular Holiday and Rest Day','Regular Holiday and Rest Day'),
    #('Night Shift Ordinary Day','Night Shift Ordinary Day'),
    #('Night Shift Rest Day, Special Day or Regular Holiday','Night Shift Rest Day, Special Day or Regular Holiday'),
    ('Vacation Leave','Vacation Leave'),
    ('Maternity Leave','Maternity Leave'), 
    ('Sick Leave','Sick Leave'),
    ('Paternity Leave','Paternity Leave'),
    ('Leave without pay','Leave without pay'),
    ('Others','Others'),
)
Computing_Overtime = (
    ('Ordinary Days','Ordinary Days'),
    ('Rest Day, Special Day, or Regular Day','Rest Day, Special Day, or Regular Day'),
    #('Night Shift Ordinary Day','Night Shift Ordinary Day'),
    #('Night Shift Rest Day, Special Day or Regular Holiday','Night Shift Rest Day, Special Day or Regular Holiday'),
)
class AttendanceInfo(models.Model):
    employee_profile = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='employee_personal_info_fk')
    cut_off_period = models.ForeignKey(CutOffPeriodInfo, on_delete=models.CASCADE, related_name='cut_off_period_fk')
    days_of_week = models.CharField(max_length=30, blank=True,  null=True, default=None)
    date = models.CharField(max_length=30, blank=True,  null=True, default=None)
    time_in = models.CharField(max_length=30, blank=True,  null=True, default=None)
    time_out = models.CharField(max_length=30, blank=True,  null=True, default=None)
    payment_computation_for_work_done = models.CharField(max_length=100, choices=Computing_Pay_for_Work_Done, default=Computing_Pay_for_Work_Done[0][0])
    late = models.CharField(max_length=30, blank=True, null=True, default=None)
    undertime = models.CharField(max_length=30, blank=True,  null=True, default=None)
    overtime = models.CharField(max_length=30, blank=True, null=True, default=None)
    payment_computation_overtime = models.CharField(max_length=100, choices=Computing_Overtime, default=Computing_Overtime[0][0] )
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cut_off_period)


class EmployeePayroll(models.Model): 
    employee_fk = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="employee_payroll_fk", null=True)
    payroll_cutoff_period = models.ForeignKey(CutOffPeriodInfo, on_delete=models.CASCADE, related_name="employee_cutoff_fk", null=True) 
    payroll_date = models.DateField(auto_now=True)
    monthly_rate = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    monthly_allowance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    basic_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    allowance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    overtime_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    legal_holiday = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    special_holiday = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    late_or_absences = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    salary_or_cash_advance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    gross_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    #deductions
    sss_premiums = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    philhealth_contribution = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    pagibig_contribution = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    withholding_tax = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    pagibig_loan = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deducted_salary_cash_advance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    total_deduction = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    net_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    thirteenth_month_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    date_added = models.DateField(auto_now_add=True, null=True)

    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.employee_fk)

class EmployeeSalary(models.Model):
    employee_salary_fk = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="employee_salary_fk", null=True)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    allowance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    reason = models.CharField(max_length=150, default="None")

    def __str__(self):
        return str(self.amount)

 
classification_of_leave_list = (
    ('Others', 'Others'),
    ('Vacation Leave', 'Vacation Leave'),
    ('Maternity Leave', 'Maternity Leave'),
    ('Sick Leave', 'Sick Leave'),
    ('Paternity Leave', 'Paternity Leave'),
    ('Leave without pay', 'Leave without pay'),
)

leave_status = (
    ('Disapproved','Disapproved'),
    ('Approved','Approved'),
)

class EmployeeLeaves(models.Model):
    employee_leave_fk = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="employee_leave_fk")
    date_filed = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=150, default="None")
    status = models.CharField(max_length=150, choices=leave_status, default=leave_status[0][0])
    no_days = models.IntegerField()
    inclusive_dates = models.CharField(max_length=100)
    reasons = models.CharField(max_length=250)
    classification_of_leave = models.CharField(max_length=100, choices=classification_of_leave_list, default=classification_of_leave_list[0][0])
    leave_credits = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    less_this_application = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    balance_as_of_this_date = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    #prepared_by = same as the name
    #https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4
    # noted_by = models.ForeignKey(PersonalInfo, on_delete=models.DO_NOTHING, related_name="nb_personal_fk", null=True, blank=True)
    # checked_by = models.ForeignKey(PersonalInfo, on_delete=models.DO_NOTHING, related_name="cb_personal_fk", null=True, blank=True)
    # approved_by = models.ForeignKey(PersonalInfo, on_delete=models.DO_NOTHING, related_name="ab_personal_fk", null=True, blank=True)
    noted_by = models.CharField(max_length=100, null=True, blank = True)
    checked_by =models.CharField(max_length=100, null=True, blank = True)
    approved_by = models.CharField(max_length=100, null=True, blank = True)

    def __str__(self):
        return str(self.employee_leave_fk)

class EmployeeItenerary(models.Model):
    employee_itenerary_fk = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="employee_itenerary_fk")
    date_filed = models.DateField(auto_now_add=True)
    noted_by = models.CharField(max_length=100, null=True, blank = True)
    checked_by =models.CharField(max_length=100, null=True, blank = True)
    approved_by = models.CharField(max_length=100, null=True, blank = True)

    def __str__(self):
        return str(self.employee_itenerary_fk)

class EmployeeIteneraryDetails(models.Model):
    employee_itenerary  = models.ForeignKey(EmployeeItenerary, on_delete=models.CASCADE, related_name="employee_itenerary")
    date = models.CharField(max_length=100)
    timeIn = models.CharField(max_length=100)
    timeOut = models.CharField(max_length=100)
    reasons = models.CharField(max_length=250)

    def __str__(self):
        return str(self.employee_itenerary)

class Concerns(models.Model):
    sender  = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="sender_fk")
    receiver  = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name="receiver_fk")
    subject = models.CharField(max_length=100)
    message =  models.TextField() 
    reply =  models.TextField(blank=True, null=True) 
    date_filed = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.subject)
category_list = (
    ('Uploading File','Uploading File'),
    ('Delete Uploaded File','Delete Uploaded File'),
    ('Creating Payroll','Creating Payroll'),
    ('Updating Payroll Settings', 'Updating Payroll Settings'),
    ('Updating Profile','Updating Profile'),
    ('Updating Password','Updating Password'),
    ('New User Registration','New User Registration'),
    ('Deleting Employee','Deleting Employee'),
    ('Reply Concerns','Reply Concerns'),
    ('Creating Employee Transaction','Creating Employee Transaction'),
    ('Updating Employee Transaction','Updating Employee Transaction'),    
    ('Deleting Employee Transaction','Deleting Employee Transaction'),
    ('Add','Add'),
    ('Delete','Delete'),
)
level_list = (
        ('success','success'), 
        ('info','info'), 
        ('warning','warning'), 
        ('error','error')
        )
class Notifications(models.Model):
    sender  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="not_sender_fk")
    recipient  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="not_receiver_fk")
    url = models.CharField(max_length=100, blank=True, null=True) 
    message =  models.TextField() 
    category = models.CharField(max_length=150, choices=category_list, default=category_list[0][0])
    level = models.CharField(max_length=150, choices=level_list, default=level_list[0][0])
    public = models.BooleanField(default=False)
    is_read  = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message