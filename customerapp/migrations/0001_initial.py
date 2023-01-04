# Generated by Django 3.2.5 on 2021-10-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]