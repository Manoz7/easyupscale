# Generated by Django 4.0.6 on 2022-07-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=100)),
                ('country', models.CharField(default='Nepal', max_length=25)),
                ('location', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('field_of_work', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('rpr_name', models.CharField(max_length=50)),
                ('rpr_post', models.CharField(max_length=50)),
            ],
        ),
    ]
