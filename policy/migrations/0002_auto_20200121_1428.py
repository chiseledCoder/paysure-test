# Generated by Django 3.0.2 on 2020-01-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='benefits',
            field=models.CharField(choices=[('dentist', 'dentist'), ('optician', 'optician'), ('gynecologist', 'gynecologist'), ('orthopedic', 'orthopedic')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='policy',
            name='benefits',
            field=models.CharField(choices=[('dentist', 'dentist'), ('optician', 'optician'), ('gynecologist', 'gynecologist'), ('orthopedic', 'orthopedic')], default=1, max_length=50),
        ),
    ]
