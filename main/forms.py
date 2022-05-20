# Формы для записи данных в модели
from django.forms import ModelForm
from .models import Employee, Post, Department
from .models import Diploma, Vacation, Promotion
from .models import Staff

# Должность
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'salarymin', 'salarymax',)
        labels = {'title' : 'Должность'}

# Отдел
class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('title', 'imp')
        labels = {'title' : 'Отдел', 'imp' : 'Ключевой отдел'}

# Сотрудник
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('pnumber', 'surname', 'name', 'midname', 'sex', 'birthday', 'address', 'phone',
            'empdate', 'dismdate', 'inn', 'salary', 'passpnum', 'passpdate', 'passporg',
            'department', 'post',)

# Документ
class DiplomaForm(ModelForm):
    class Meta:
        model = Diploma
        fields = ('institution', 'endyear', 'dtype', 'qualif',)

# Отпуск
class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ('vtype', 'startdate', 'duration', 'ordernum',)

class Vac2Form(ModelForm):
    class Meta:
        model = Vacation
        fields = ('employee', 'vtype', 'startdate', 'duration', 'ordernum',)

# Поощрение
class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ('ptype', 'pdate', 'reason', 'summ', 'ordernum',)

class Prom2Form(ModelForm):
    class Meta:
        model = Promotion
        fields = ('employee', 'ptype', 'pdate', 'reason', 'summ', 'ordernum',)

# Штатное расписание
class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ('department', 'post', 'num')
