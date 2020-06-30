# Generated by Django 2.2.3 on 2020-05-19 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_cutoffperiodinfo_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePayroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payroll_cutoff_period', models.CharField(blank=True, max_length=50)),
                ('payroll_date', models.DateField()),
                ('monthly_rate', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('monthly_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('basic_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('overtime_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('legal_holiday', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('special_holiday', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('late_or_absences', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('salary_or_cash_advance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('gross_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('sss_premiums', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('philhealth_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('pagibig_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('withholding_tax', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('pagibig_loan', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_deduction', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('net_pay', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('employee_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_payroll_fk', to='application.PersonalInfo')),
            ],
        ),
    ]
