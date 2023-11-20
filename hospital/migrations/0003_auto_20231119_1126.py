# Generated by Django 3.0.5 on 2023-11-19 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20231118_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_discharge', to='hospital.Appointment'),
        ),
    ]
