# Generated by Django 4.0 on 2021-12-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('comment', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]