# Generated by Django 2.2.3 on 2020-05-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0016_auto_20200519_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepayroll',
            name='thirteenth_month_pay',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
