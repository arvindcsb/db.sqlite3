# Generated by Django 4.0.4 on 2022-05-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsapp', '0002_auto_20220518_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
