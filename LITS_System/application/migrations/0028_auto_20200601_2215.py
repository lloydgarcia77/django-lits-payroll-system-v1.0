# Generated by Django 2.2.3 on 2020-06-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_auto_20200601_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleaves',
            name='status',
            field=models.CharField(choices=[('Disapproved', 'Disapproved'), ('Approved', 'Approved')], default='Disapproved', max_length=150),
        ),
    ]
