# Generated by Django 4.1.2 on 2022-11-04 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0002_remove_uslugi_title_uslugi_hour_from_uslugi_hour_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uslugi',
            name='hour_from',
        ),
        migrations.RemoveField(
            model_name='uslugi',
            name='hour_to',
        ),
        migrations.RemoveField(
            model_name='uslugi',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='uslugi',
            name='working_days',
        ),
    ]