# Generated by Django 4.1.6 on 2023-12-19 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0015_alter_password_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pwconfigattachments',
            name='APP_NAME',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list'),
        ),
    ]