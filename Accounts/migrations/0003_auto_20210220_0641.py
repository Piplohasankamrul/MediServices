# Generated by Django 3.1 on 2021-02-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_doctorprofile_driverprofile_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]
