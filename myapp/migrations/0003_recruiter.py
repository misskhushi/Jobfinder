# Generated by Django 3.2.13 on 2023-02-09 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_alter_jobseeker_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
