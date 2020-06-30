# Generated by Django 2.2.3 on 2020-04-29 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20200429_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='CutOffPeriodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_file', models.FileField(upload_to='documents/%Y/%m/%d', verbose_name='Attendance .xlsx file')),
                ('cut_off_period', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('date', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('time_in', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('time_out', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('late', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('undertime', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('overtime', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('cut_off_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cut_off_period_fk', to='application.CutOffPeriodInfo')),
                ('employee_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_personal_info_fk', to='application.PersonalInfo')),
            ],
        ),
    ]