# Generated by Django 4.1.6 on 2023-12-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0018_passwordpolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordpolicy',
            name='CREATED_BY',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passwordpolicy',
            name='CREATED_ON',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='passwordpolicy',
            name='LAST_MODIFIED',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='passwordpolicy',
            name='MODIFIED_BY',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
