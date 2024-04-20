# Generated by Django 5.0.4 on 2024-04-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0028_integration_accounts_system_accounts'),
    ]

    operations = [
        migrations.CreateModel(
            name='PASSWORDCONFIG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MIN_LENGTH', models.CharField(blank=True, max_length=100, null=True)),
                ('HISTORY', models.CharField(blank=True, max_length=100, null=True)),
                ('AGE', models.CharField(blank=True, max_length=100, null=True)),
                ('LOCKOUT', models.CharField(blank=True, max_length=100, null=True)),
                ('COMPLEXITY_ENABLED', models.BooleanField(blank=True, null=True)),
                ('HAS_SPECIALCHAR', models.BooleanField(blank=True, null=True)),
                ('HAS_NUMERIC', models.BooleanField(blank=True, null=True)),
                ('HAS_UPPER', models.BooleanField(blank=True, null=True)),
                ('HAS_LOWER', models.BooleanField(blank=True, null=True)),
                ('MFA_ENABLED', models.BooleanField(blank=True, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'SYS_PWCONFIG',
                'managed': True,
            },
        ),
    ]
