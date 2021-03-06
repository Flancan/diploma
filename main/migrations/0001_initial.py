# Generated by Django 3.2.9 on 2022-05-12 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('imp', models.BooleanField(default=False, verbose_name='Ключевой отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnumber', models.CharField(max_length=15, unique=True, verbose_name='Табельный номер')),
                ('surname', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('midname', models.CharField(max_length=25, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], max_length=1, verbose_name='Пол')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Телефон')),
                ('empdate', models.DateField(verbose_name='Дата поступления')),
                ('dismdate', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('inn', models.BigIntegerField(null=True, unique=True, verbose_name='ИНН')),
                ('salary', models.IntegerField(verbose_name='Оклад')),
                ('passpnum', models.CharField(max_length=15, unique=True, verbose_name='Номер паспорта')),
                ('passpdate', models.DateField(verbose_name='Дата выдачи')),
                ('passporg', models.CharField(max_length=50, verbose_name='Кем выдан')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'ordering': ['pnumber'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('salarymin', models.IntegerField(verbose_name='Минимальный оклад')),
                ('salarymax', models.IntegerField(verbose_name='Максимальный оклад')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtype', models.CharField(max_length=20, verbose_name='Вид отпуска')),
                ('startdate', models.DateField(verbose_name='Дата начала')),
                ('duration', models.IntegerField(verbose_name='Продолжительность')),
                ('ordernum', models.CharField(max_length=20, verbose_name='Номер приказа')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Отпуск',
                'verbose_name_plural': 'Отпуски',
                'ordering': ['startdate'],
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('exp', models.FloatField(verbose_name='Расходы')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Расход на зарплату',
                'verbose_name_plural': 'Расходы на зарплату',
                'ordering': ['department', 'year'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=20, verbose_name='Вид поощрения')),
                ('pdate', models.DateField(verbose_name='Дата')),
                ('reason', models.CharField(max_length=30, verbose_name='Причина')),
                ('summ', models.IntegerField(null=True, verbose_name='Вознаграждение')),
                ('ordernum', models.CharField(max_length=20, null=True, verbose_name='Номер приказа')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Поощрение',
                'verbose_name_plural': 'Поощрения',
                'ordering': ['pdate'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.post', verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=30, verbose_name='Учреждение')),
                ('endyear', models.IntegerField(verbose_name='Год окончания')),
                ('dtype', models.CharField(max_length=20, verbose_name='Вид образования')),
                ('qualif', models.CharField(max_length=30, verbose_name='Квалификация')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'ОбрДокумент',
                'verbose_name_plural': 'ОбрДокументы',
                'ordering': ['endyear'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='Кол-во позиций')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department', verbose_name='Отдел')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.post', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Штатное расписание',
                'verbose_name_plural': 'Штатные расписания',
                'ordering': ['department', 'post'],
                'unique_together': {('department', 'post')},
            },
        ),
    ]
