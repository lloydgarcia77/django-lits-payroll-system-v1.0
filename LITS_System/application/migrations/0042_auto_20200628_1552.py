# Generated by Django 2.2.3 on 2020-06-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0041_auto_20200628_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='category',
            field=models.CharField(choices=[('Uploading File', 'Uploading File'), ('Delete Uploaded File', 'Delete Uploaded File'), ('Creating Payroll', 'Creating Payroll'), ('Updating Payroll Settings', 'Updating Payroll Settings'), ('Updating Profile', 'Updating Profile'), ('Updating Password', 'Updating Password'), ('New User Registration', 'New User Registration'), ('Deleting Employee', 'Deleting Employee'), ('Reply Concerns', 'Reply Concerns'), ('Creating Employee Transaction', 'Creating Employee Transaction'), ('Updating Employee Transaction', 'Updating Employee Transaction'), ('Deleting Employee Transaction', 'Deleting Employee Transaction')], default='Uploading File', max_length=150),
        ),
    ]