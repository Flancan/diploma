from tabnanny import verbose
from django.db import models
from django.forms import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from django.db.models import Q, Min, Max, Avg

# Отделы
class Department(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Название')
    imp = models.BooleanField(null=False, default=False, verbose_name='Ключевой отдел')

    def __str__(self):
        return self.title

    def ave(self):
        emps = Employee.objects.filter(department=self.pk, dismdate__isnull=True) \
            .aggregate(ave=Avg('salary', output_field=models.FloatField()))
        return emps['ave']

    class Meta:
        verbose_name_plural = 'Отделы'
        verbose_name = 'Отдел'
        ordering = ['title']

# Должности
class Post(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Название')
    salarymin = models.IntegerField(verbose_name='Минимальный оклад')
    salarymax = models.IntegerField(verbose_name='Максимальный оклад')
    dep = -1

    def __str__(self):
        return self.title

    def ave(self):
        cond = Q(dismdate__isnull=True) & Q(post=self.pk)
        if self.dep >= 0:
            cond = cond & Q(department=self.dep)
        emps = Employee.objects.filter(cond) \
            .aggregate(ave=Avg('salary', output_field=models.FloatField()))
        return emps['ave']

    class Meta:
        verbose_name_plural = 'Должности'
        verbose_name = 'Должность'
        ordering = ['title']

# Работники
class Employee(models.Model):
    DSEX = (('m', 'Мужской'), ('f', 'Женский'))
    pnumber = models.CharField(max_length=15, unique=True, verbose_name='Табельный номер')
    surname = models.CharField(max_length=25, verbose_name='Фамилия')
    name = models.CharField(max_length=25, verbose_name='Имя')
    midname = models.CharField(max_length=25, verbose_name='Отчество')
    sex = models.CharField(max_length=1, choices=DSEX, verbose_name='Пол')
    birthday = models.DateField(verbose_name='Дата рождения')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(null=True, max_length=20, verbose_name='Телефон')
    empdate = models.DateField(verbose_name='Дата поступления')
    dismdate = models.DateField(null=True, blank=True, verbose_name='Дата увольнения')
    inn = models.BigIntegerField(unique=True, null=True, verbose_name='ИНН')
    salary = models.IntegerField(verbose_name='Оклад')
    passpnum = models.CharField(max_length=15, unique=True, verbose_name='Номер паспорта')
    passpdate = models.DateField(verbose_name='Дата выдачи')
    passporg = models.CharField(max_length=50, verbose_name='Кем выдан')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отдел')
    post = models.ForeignKey('Post', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return self.surname + ' ' + self.name[:1:] + '. ' + self.midname[:1:] + '.'

    def edu(self):
        return Diploma.objects.get(employee=self.pk).dtype
    
    def deppost(self):
        return f'{self.department}-{self.post}'

    def clean(self):
        errors = {}
        pos = Staff.objects.filter(department=self.department, post=self.post).first()
        if ((not pos) or (pos.num <= pos.workers())) and self.pk is None:
            errors[NON_FIELD_ERRORS] = ValidationError('Для сотрудника нет места в штате.')
        if errors:
            raise ValidationError(errors)


    class Meta:
        verbose_name_plural = 'Работники'
        verbose_name = 'Работник'
        ordering = ['pnumber']

# Образование
class Diploma(models.Model):
    institution = models.CharField(max_length=30, verbose_name='Учреждение')
    endyear = models.IntegerField(verbose_name='Год окончания')
    dtype = models.CharField(max_length=20, verbose_name='Вид образования')
    qualif = models.CharField(max_length=30, verbose_name='Квалификация')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.institution}, {self.endyear} - {self.qualif}'

    class Meta:
        verbose_name_plural = 'ОбрДокументы'
        verbose_name = 'ОбрДокумент'
        ordering = ['endyear']

# Отпуск
class Vacation(models.Model):
    vtype = models.CharField(max_length=20, verbose_name='Вид отпуска')
    startdate = models.DateField(verbose_name='Дата начала')
    duration = models.IntegerField(verbose_name='Продолжительность')
    ordernum = models.CharField(max_length=20, verbose_name='Номер приказа')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.startdate} - {self.duration}'

    class Meta:
        verbose_name_plural = 'Отпуски'
        verbose_name = 'Отпуск'
        ordering = ['startdate']

# Поощрение
class Promotion(models.Model):
    ptype = models.CharField(max_length=20, verbose_name='Вид поощрения')
    pdate = models.DateField(verbose_name='Дата')
    reason = models.CharField(max_length=30, verbose_name='Причина')
    summ = models.IntegerField(null=True, verbose_name='Вознаграждение')
    ordernum = models.CharField(max_length=20, null=True, verbose_name='Номер приказа')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.ptype}, {self.pdate}'

    class Meta:
        verbose_name_plural = 'Поощрения'
        verbose_name = 'Поощрение'
        ordering = ['pdate']

# Штатное расписание
class Staff(models.Model):
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отдел')
    post = models.ForeignKey('Post', on_delete=models.PROTECT, verbose_name='Должность')
    num = models.IntegerField(null=False, verbose_name='Кол-во позиций')

    def __str__(self):
        return f'{self.department}, {self.post}, {self.num}'

    def workers(self):
        n = Employee.objects.filter(department=self.department, 
            post=self.post, dismdate__isnull=True).count()
        return n

    class Meta:
        verbose_name_plural = 'Штатные расписания'
        verbose_name = 'Штатное расписание'
        ordering = ['department', 'post']
        unique_together = ('department', 'post',)

# Расходы на зарплату в предыдущие годы
class Salary(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Отдел')
    year = models.IntegerField(verbose_name='Год')
    exp = models.FloatField(verbose_name='Расходы')

    def __str__(self):
        return f'{self.department.title}{self.year}{self.exp: .2f}'

    class Meta:
        verbose_name_plural = 'Расходы на зарплату'
        verbose_name = 'Расход на зарплату'
        ordering = ['department', 'year']
