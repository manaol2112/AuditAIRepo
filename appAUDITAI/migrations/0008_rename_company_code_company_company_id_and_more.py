# Generated by Django 4.1.6 on 2023-12-03 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0007_remove_company_company_id_company_company_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='COMPANY_CODE',
            new_name='COMPANY_ID',
        ),
        migrations.RenameField(
            model_name='userroles',
            old_name='COMPANY_CODE',
            new_name='COMPANY_ID',
        ),
    ]