# Generated by Django 4.1.2 on 2022-11-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uslugi',
            name='title',
        ),
        migrations.AddField(
            model_name='uslugi',
            name='hour_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='hour_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uslugi',
            name='working_days',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
