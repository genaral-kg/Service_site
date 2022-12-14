# Generated by Django 4.1.2 on 2022-11-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_city_delete_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='about_me',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='category',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='passwordImage',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='video',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
