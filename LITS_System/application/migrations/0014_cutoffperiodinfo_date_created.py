# Generated by Django 2.2.3 on 2020-05-02 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_attendanceinfo_cutoffperiodinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutoffperiodinfo',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]