# Generated by Django 4.1.2 on 2022-11-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_customuser_about_me_remove_customuser_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
