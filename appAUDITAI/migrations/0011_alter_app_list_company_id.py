# Generated by Django 4.1.6 on 2023-12-09 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0010_remove_userroles_is_locked_remove_userroles_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_list',
            name='COMPANY_ID',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.company'),
        ),
    ]
