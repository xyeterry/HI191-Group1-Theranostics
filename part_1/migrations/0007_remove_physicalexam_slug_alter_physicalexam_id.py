# Generated by Django 4.2.3 on 2023-08-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0006_physicalexam_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physicalexam',
            name='slug',
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
