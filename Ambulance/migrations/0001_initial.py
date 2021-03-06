# Generated by Django 3.1 on 2021-02-22 16:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0003_auto_20210220_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbulanceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='category/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Ambulance.ambulancecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ambulace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='driver/')),
                ('discription', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='New', max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ambulance.ambulancecategory')),
                ('driver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.driverprofile')),
            ],
        ),
    ]
