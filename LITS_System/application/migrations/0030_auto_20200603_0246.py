# Generated by Django 2.2.3 on 2020-06-02 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0029_auto_20200602_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleaves',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ab_personal_fk', to='application.PersonalInfo'),
        ),
        migrations.AlterField(
            model_name='employeeleaves',
            name='checked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cb_personal_fk', to='application.PersonalInfo'),
        ),
        migrations.AlterField(
            model_name='employeeleaves',
            name='noted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nb_personal_fk', to='application.PersonalInfo'),
        ),
    ]
