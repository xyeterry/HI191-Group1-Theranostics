# Generated by Django 4.0.4 on 2023-01-20 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0012_alter_patient_patient_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='physicalexam',
            old_name='patient_name',
            new_name='patient',
        ),
    ]
