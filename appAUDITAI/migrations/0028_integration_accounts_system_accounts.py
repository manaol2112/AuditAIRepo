# Generated by Django 5.0.4 on 2024-04-15 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0027_alter_admin_roles_filter_app_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='INTEGRATION_ACCOUNTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_INTEGRATION_ACCOUNT', models.BooleanField(blank=True, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
                ('USER_ID', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_record')),
            ],
        ),
        migrations.CreateModel(
            name='SYSTEM_ACCOUNTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IS_SYSTEM_ACCOUNT', models.BooleanField(blank=True, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
                ('USER_ID', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_record')),
            ],
        ),
    ]
