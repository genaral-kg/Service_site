# Generated by Django 4.1.2 on 2022-11-03 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
