# Generated by Django 4.1.4 on 2023-01-14 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0008_alter_workers_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Professions',
            },
        ),
        migrations.AddField(
            model_name='workers',
            name='condition_class',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Класс условий труда'),
        ),
        migrations.AddField(
            model_name='workers',
            name='dangerous_factors',
            field=models.CharField(blank=True, choices=[('Пыль растительного происхождения (А): древесина, пр.1, п.2.7;', 'Пыль растительного происхождения (А): древесина, пр.1, п.2.7;'), ('Работы на механическом оборудовании, пр.3 п.12', 'Работы на механическом оборудовании, пр.3 п.12'), ('Работа на высоте, пр.3 п.1.', 'Работа на высоте, пр.3 п.1.'), ('Производственный шум, пр.1 п.4.4;', 'Производственный шум, пр.1 п.4.4;'), ('Тепловое излучение, пр. 1 п.4.9.', 'Тепловое излучение, пр. 1 п.4.9.'), ('Работы, связанные с оптическими приборами при длительности сосредоточенного наблюдения более 50 % времени рабочей смены пр.1 п.5.6', 'Работы, связанные с оптическими приборами при длительности сосредоточенного наблюдения более 50 % времени рабочей смены пр.1 п.5.6'), ('Повышенная температура воздуха, пр. 1 п.4.8.', 'Повышенная температура воздуха, пр. 1 п.4.8.'), ('Углеводороды ароматические: бензол (К), толуол, ксилол, стирол и другие, пр.1, п.1.1.31.', 'Углеводороды ароматические: бензол (К), толуол, ксилол, стирол и другие, пр.1, п.1.1.31.'), ('Альдегиды алифатические (предельные, непредельные и ароматические): формальдегид (К, А), ацетальдегид, акролеин, бензальдегид, фталевый (А), глутаровый альдегид (А), пр.1, п.1.1.2.', 'Альдегиды алифатические (предельные, непредельные и ароматические): формальдегид (К, А), ацетальдегид, акролеин, бензальдегид, фталевый (А), глутаровый альдегид (А), пр.1, п.1.1.2.')], max_length=200, null=True, verbose_name='Вредные и опасные факторы'),
        ),
        migrations.AddField(
            model_name='workers',
            name='frequency',
            field=models.CharField(blank=True, choices=[('1 раз в 2 года', '1 раз в 2 года'), ('1 раз в год', '1 раз в год')], max_length=20, null=True, verbose_name='Периодичность проведения медицинского осмотра'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workers.professions'),
        ),
        migrations.DeleteModel(
            name='MedicalExamination',
        ),
    ]
