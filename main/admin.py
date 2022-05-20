from re import search
from django.contrib import admin

# Регистрация моделей на /admin
from .models import Department
from .models import Post
from .models import Employee
from .models import Diploma
from .models import Vacation
from .models import Promotion
from .models import Staff
from .models import Salary

# Редакторы моделей для /admin
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    # Поля, по которым будет выполняться фильтрация
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pnumber', 'surname', 'name',)
    list_display_links = ('pnumber', 'surname',)
    search_fields = ('pnumber', 'surname')

class DiplomaAdmin(admin.ModelAdmin):
    list_display = ('employee', 'endyear', 'dtype',)
    list_display_links = ('employee',)
    search_fields = ('employee', 'dtype',)

class VacationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'vtype', 'startdate',)
    list_display_links = ('employee',)
    search_fields = ('employee',)

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'ptype', 'pdate',)
    list_display_links = ('employee',)
    search_fields = ('employee',)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('department', 'post', 'num',)
    list_display_links = ('department',)
    search_fields = ('department',)

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('department', 'year', 'exp',)
    list_display_links = ('department', 'year')
    search_fields = ('department', 'year')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Diploma, DiplomaAdmin)
admin.site.register(Vacation, VacationAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Salary, SalaryAdmin)
