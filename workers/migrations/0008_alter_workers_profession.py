# Generated by Django 4.1.4 on 2023-01-14 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_medicalexamination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.medicalexamination'),
        ),
    ]
