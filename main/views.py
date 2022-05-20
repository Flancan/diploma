from datetime import datetime, date, timedelta
from multiprocessing import context
from django.forms import IntegerField
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post, Department, Employee, Diploma, Salary
from .models import Vacation, Promotion
from .models import Staff
from main.forms import PostForm, DepartmentForm, EmployeeForm
from main.forms import DiplomaForm, VacationForm, PromotionForm
from main.forms import StaffForm
from main.forms import Vac2Form
from main.forms import Prom2Form

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models import Min, Max, Avg

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    # return render(request, 'main/index.html', {})
    return HttpResponseRedirect(reverse('showemps'))

# -------------------- "Должность" --------------------
# Отображение списка должностей
@login_required
def showposts(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'main/posts.html', context)

# Добавление новой должности
@login_required
def addpost(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        postf = PostForm(request.POST)
        if postf.is_valid():
           postf.save()
           return HttpResponseRedirect(reverse('showposts'))
        else:
            context = {'form' : postf, 'button_label' : button_label}
            return render(request, 'main/form_post.html', context)
    else:
        postf = PostForm()
        context = {'form' : postf, 'button_label' : button_label}
        return render(request, 'main/form_post.html', context)

# Отображение информации/изменение должности
@login_required
def editpost(request, post_id):
    button_label = 'Сохранить'
    rec = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        postf = PostForm(request.POST, instance=rec)
        if postf.is_valid():
            postf.save()
            return HttpResponseRedirect(reverse('showposts'))
        else:
            context = {'form' : postf, 'button_label' : button_label}
            return render(request, 'main/form_post.html', context)
    else:
        postf = PostForm(instance=rec)
        context = {'form' : postf, 'button_label' : button_label}
        return render(request, 'main/form_post.html', context)

# Удаление должности
@login_required
def delpost(request, post_id):
    rec = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showposts'))
    else:
        context = {'post' : rec}
        return render(request, 'main/form_post_confirm.html', context)

# -------------------- "Отдел" --------------------
# Отображение списка отделов
@login_required
def showdeps(request):
    deps = Department.objects.all()
    context = {'deps' : deps}
    return render(request, 'main/deps.html', context)

# Добавление нового отдела
@login_required
def adddep(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        depf = DepartmentForm(request.POST)
        if depf.is_valid():
           depf.save()
           return HttpResponseRedirect(reverse('showdeps'))
        else:
            context = {'form' : depf, 'button_label' : button_label}
            return render(request, 'main/form_dep.html', context)
    else:
        depf = DepartmentForm()
        context = {'form' : depf, 'button_label' : button_label}
        return render(request, 'main/form_dep.html', context)

# Отображение информации/изменение отдела
@login_required
def editdep(request, dep_id):
    button_label = 'Сохранить'
    rec = Department.objects.get(pk=dep_id)
    if request.method == 'POST':
        depf = DepartmentForm(request.POST, instance=rec)
        if depf.is_valid():
            depf.save()
            return HttpResponseRedirect(reverse('showdeps'))
        else:
            context = {'form' : depf, 'button_label' : button_label}
            return render(request, 'main/form_dep.html', context)
    else:
        depf = DepartmentForm(instance=rec)
        context = {'form' : depf, 'button_label' : button_label}
        return render(request, 'main/form_dep.html', context)

# Удаление отдела
@login_required
def deldep(request, dep_id):
    rec = Department.objects.get(pk=dep_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showdeps'))
    else:
        context = {'dep' : rec}
        return render(request, 'main/form_dep_confirm.html', context)

# -------------------- "Сотрудник" --------------------
# Отображение списка сотрудников
@login_required
def showemps(request):
    emps = Employee.objects.filter(dismdate__isnull=True)
    context = {'emps' : emps}
    return render(request, 'main/emps.html', context)

# Отображение уволенных
@login_required
def showdisms(request):
    emps = Employee.objects.filter(dismdate__isnull=True)
    disms = Employee.objects.filter(dismdate__isnull=False)
    context = {'emps' : emps, 'disms': disms}
    return render(request, 'main/disms.html', context)

# Добавление нового сотрудника
@login_required
def addemp(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        empf = EmployeeForm(request.POST)
        if empf.is_valid():
           empf.save()
           return HttpResponseRedirect(reverse('showemps'))
        else:
            context = {'form' : empf, 'button_label' : button_label}
            return render(request, 'main/form_emp.html', context)
    else:
        empf = EmployeeForm()
        context = {'form' : empf, 'button_label' : button_label}
        return render(request, 'main/form_emp.html', context)

# Отображение информации/изменение сотрудника
@login_required
def editemp(request, emp_id):
    button_label = 'Сохранить'
    dips = Diploma.objects.filter(employee=emp_id)
    vacs = Vacation.objects.filter(employee=emp_id)
    proms = Promotion.objects.filter(employee=emp_id)
    rec = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        empf = EmployeeForm(request.POST, instance=rec)
        if empf.is_valid():
            empf.save()
            return HttpResponseRedirect(reverse('showemps'))
        else:
            context = {'form' : empf, 'dips' : dips, 'button_label' : button_label, 
                'emp_id' : emp_id, 'vacs' : vacs, 'proms' : proms}
            return render(request, 'main/form_emp.html', context)
    else:
        empf = EmployeeForm(instance=rec)
        context = {'form' : empf, 'dips' : dips, 'button_label' : button_label,
            'emp_id' : emp_id, 'vacs' : vacs, 'proms' : proms}
        return render(request, 'main/form_emp.html', context)

# Удаление сотрудника
@login_required
def delemp(request, emp_id):
    rec = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showemps'))
    else:
        context = {'emp' : rec}
        return render(request, 'main/form_emp_confirm.html', context)

# -------------------- "ОбрДокумент" --------------------
# Добавление нового документа
@login_required
def adddip(request, emp_id):
    button_label = 'Добавить'
    rec = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        dipf = DiplomaForm(request.POST)
        if dipf.is_valid():
            # Добавление идентификатора сотрудника
            dip = dipf.save(commit=False)
            dip.employee = rec
            dip.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : dipf, 'button_label' : button_label, 'emp' : rec}
            return render(request, 'main/form_dip.html', context)
    else:
        dipf = DiplomaForm()
        context = {'form' : dipf, 'button_label' : button_label, 'emp' : rec}
        return render(request, 'main/form_dip.html', context)

# Отображение информации/изменение документа
@login_required
def editdip(request, dip_id):
    button_label = 'Сохранить'
    rec = Diploma.objects.get(pk=dip_id)
    emp_id = rec.employee.pk
    emp = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        dipf = DiplomaForm(request.POST, instance=rec)
        if dipf.is_valid():
            dip = dipf.save(commit=False)
            dip.employee = emp
            dip.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : dipf, 'button_label' : button_label, 'emp' : emp}
            return render(request, 'main/form_dip.html', context)
    else:
        dipf = DiplomaForm(instance=rec)
        context = {'form' : dipf, 'button_label' : button_label, 'emp' : emp}
        return render(request, 'main/form_dip.html', context)

# Удаление документа
@login_required
def deldip(request, dip_id):
    rec = Diploma.objects.get(pk=dip_id)
    emp_id = rec.employee.pk
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
    else:
        context = {'dip' : rec}
        return render(request, 'main/form_dip_confirm.html', context)

# -------------------- "Отпуск" --------------------
# Добавление нового отпуска
@login_required
def addvac(request, emp_id):
    button_label = 'Добавить'
    rec = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        vacf = VacationForm(request.POST)
        if vacf.is_valid():
            # Добавление идентификатора сотрудника
            vac = vacf.save(commit=False)
            vac.employee = rec
            vac.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : vacf, 'button_label' : button_label, 'emp' : rec}
            return render(request, 'main/form_vac.html', context)
    else:
        vacf = VacationForm()
        context = {'form' : vacf, 'button_label' : button_label, 'emp' : rec}
        return render(request, 'main/form_vac.html', context)

# Отображение информации/изменение отпуска
@login_required
def editvac(request, vac_id):
    button_label = 'Сохранить'
    rec = Vacation.objects.get(pk=vac_id)
    emp_id = rec.employee.pk
    emp = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        vacf = VacationForm(request.POST, instance=rec)
        if vacf.is_valid():
            vac = vacf.save(commit=False)
            vac.employee = emp
            vac.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : vacf, 'button_label' : button_label, 'emp' : emp}
            return render(request, 'main/form_vac.html', context)
    else:
        vacf = VacationForm(instance=rec)
        context = {'form' : vacf, 'button_label' : button_label, 'emp' : emp}
        return render(request, 'main/form_vac.html', context)

# Удаление отпуска
@login_required
def delvac(request, vac_id):
    rec = Vacation.objects.get(pk=vac_id)
    emp_id = rec.employee.pk
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
    else:
        context = {'vac' : rec}
        return render(request, 'main/form_vac_confirm.html', context)

# -------------------- "Поощрение" --------------------
# Добавление нового поощрения
@login_required
def addprom(request, emp_id):
    button_label = 'Добавить'
    rec = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        promf = PromotionForm(request.POST)
        if promf.is_valid():
            # Добавление идентификатора сотрудника
            prom = promf.save(commit=False)
            prom.employee = rec
            prom.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : promf, 'button_label' : button_label, 'emp' : rec}
            return render(request, 'main/form_prom.html', context)
    else:
        promf = PromotionForm()
        context = {'form' : promf, 'button_label' : button_label, 'emp' : rec}
        return render(request, 'main/form_prom.html', context)

# Отображение информации/изменение поощрения
@login_required
def editprom(request, prom_id):
    button_label = 'Сохранить'
    rec = Promotion.objects.get(pk=prom_id)
    emp_id = rec.employee.pk
    emp = Employee.objects.get(pk=emp_id)
    if request.method == 'POST':
        promf = PromotionForm(request.POST, instance=rec)
        if promf.is_valid():
            prom = promf.save(commit=False)
            prom.employee = emp
            prom.save()
            return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
        else:
            context = {'form' : promf, 'button_label' : button_label, 'emp' : emp}
            return render(request, 'main/form_prom.html', context)
    else:
        promf = PromotionForm(instance=rec)
        context = {'form' : promf, 'button_label' : button_label, 'emp' : emp}
        return render(request, 'main/form_prom.html', context)

# Удаление поощрения
@login_required
def delprom(request, prom_id):
    rec = Promotion.objects.get(pk=prom_id)
    emp_id = rec.employee.pk
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('editemp', kwargs={'emp_id' : emp_id}))
    else:
        context = {'prom' : rec}
        return render(request, 'main/form_prom_confirm.html', context)


# -------------------- "Штатное расписание" --------------------
# Отображение штатного расписания
@login_required
def showstaff(request):
    posts = Staff.objects.all()
    context = {'staff' : posts}
    return render(request, 'main/staff.html', context)

# Добавление элемента штатного расписания
@login_required
def addstaff(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        recf = StaffForm(request.POST)
        if recf.is_valid():
           recf.save()
           return HttpResponseRedirect(reverse('showstaff'))
        else:
            context = {'form' : recf, 'button_label' : button_label}
            return render(request, 'main/form_staff.html', context)
    else:
        recf = StaffForm()
        context = {'form' : recf, 'button_label' : button_label}
        return render(request, 'main/form_staff.html', context)


# Изменение элемента штатного расписания
@login_required
def editstaff(request, staff_id):
    button_label = 'Сохранить'
    rec = Staff.objects.get(pk=staff_id)
    if request.method == 'POST':
        recf = StaffForm(request.POST, instance=rec)
        if recf.is_valid():
            recf.save()
            return HttpResponseRedirect(reverse('showstaff'))
        else:
            context = {'form' : recf, 'button_label' : button_label}
            return render(request, 'main/form_staff.html', context)
    else:
        recf = StaffForm(instance=rec)
        context = {'form' : recf, 'button_label' : button_label}
        return render(request, 'main/form_staff.html', context)

# Удаление элемента штатного расписания
@login_required
def delstaff(request, staff_id):
    rec = Staff.objects.get(pk=staff_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showstaff'))
    else:
        context = {'staff' : rec}
        return render(request, 'main/form_staff_confirm.html', context)

# -------------------- "Отпуска 2" --------------------
# Отображение отпусков
@login_required
def showvacs(request):
    vacs = Vacation.objects.all()
    context = {'vacs' : vacs}
    return render(request, 'main/vacs2.html', context)

# Добавление отпуска
@login_required
def add2vac(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        vac2f = Vac2Form(request.POST)
        if vac2f.is_valid():
           vac2f.save()
           return HttpResponseRedirect(reverse('showvacs'))
        else:
            context = {'form' : vac2f, 'button_label' : button_label}
            return render(request, 'main/form_vac2.html', context)
    else:
        vac2f = Vac2Form()
        context = {'form' : vac2f, 'button_label' : button_label}
        return render(request, 'main/form_vac2.html', context)

# Изменение отпуска
@login_required
def edit2vac(request, vac_id):
    button_label = 'Сохранить'
    rec = Vacation.objects.get(pk=vac_id)
    if request.method == 'POST':
        vac2f = Vac2Form(request.POST, instance=rec)
        if vac2f.is_valid():
            vac2f.save()
            return HttpResponseRedirect(reverse('showvacs'))
        else:
            context = {'form' : vac2f, 'button_label' : button_label}
            return render(request, 'main/form_vac2.html', context)
    else:
        vac2f = Vac2Form(instance=rec)
        context = {'form' : vac2f, 'button_label' : button_label}
        return render(request, 'main/form_vac2.html', context)

# Удаление отпуска
@login_required
def del2vac(request, vac_id):
    rec = Vacation.objects.get(pk=vac_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showvacs'))
    else:
        context = {'vac' : rec}
        return render(request, 'main/form_vac2_confirm.html', context)

# -------------------- "Поощрения 2" --------------------
# Отображение поощрений
@login_required
def showproms(request):
    proms = Promotion.objects.all()
    context = {'proms' : proms}
    return render(request, 'main/proms2.html', context)

# Добавления поощрения
@login_required
def add2prom(request):
    button_label = 'Добавить'
    if request.method == 'POST':
        prom2f = Prom2Form(request.POST)
        if prom2f.is_valid():
           prom2f.save()
           return HttpResponseRedirect(reverse('showproms'))
        else:
            context = {'form' : prom2f, 'button_label' : button_label}
            return render(request, 'main/form_prom2.html', context)
    else:
        prom2f = Prom2Form()
        context = {'form' : prom2f, 'button_label' : button_label}
        return render(request, 'main/form_prom2.html', context)

# Изменение поощрения
@login_required
def edit2prom(request, prom_id):
    button_label = 'Сохранить'
    rec = Promotion.objects.get(pk=prom_id)
    if request.method == 'POST':
        prom2f = Prom2Form(request.POST, instance=rec)
        if prom2f.is_valid():
            prom2f.save()
            return HttpResponseRedirect(reverse('showproms'))
        else:
            context = {'form' : prom2f, 'button_label' : button_label}
            return render(request, 'main/form_prom2.html', context)
    else:
        prom2f = Prom2Form(instance=rec)
        context = {'form' : prom2f, 'button_label' : button_label}
        return render(request, 'main/form_prom2.html', context)

# Удаление поощрения
@login_required
def del2prom(request, prom_id):
    rec = Promotion.objects.get(pk=prom_id)
    if request.method == 'POST':
        rec.delete()
        return HttpResponseRedirect(reverse('showproms'))
    else:
        context = {'prom' : rec}
        return render(request, 'main/form_prom2_confirm.html', context)

# -------------------- "Статистика" --------------------
@login_required
def showstat(request):
    return HttpResponseRedirect(reverse('showstatemp'))

# Пенсионеры
@login_required
def show_stat_pens(request):
    nd = date.today()
    m_date = nd - timedelta(365 * 65)
    w_date = nd - timedelta(365 * 60)
    cond = (Q(sex='m') & Q(birthday__lt=m_date)) | \
        (Q(sex='f') & Q(birthday__lt=w_date))
    # Не показывать уволенных сотрудников
    c_emp = Q(dismdate__isnull=True)

    emps = Employee.objects.filter(cond & c_emp)
    context = {'emps' : emps}
    return render(request, 'main/stat_pens.html', context)

# Сотрудники с максимальным стажем
@login_required
def show_stat_wtime(request):
    res = Employee.objects.filter(dismdate__isnull=True).aggregate(min_date=Min('empdate'))
    s_year = res['min_date'].year
    s_date = date(s_year, 1, 1)
    e_date = date(s_year, 12, 31)
    d_cond = Q(empdate__lte=e_date) & Q(empdate__gte=s_date) & Q(dismdate__isnull=True)
    stage = date.today().year - s_year
    emps = Employee.objects.filter(d_cond)
    context = {'emps' : emps, 'stage' : stage}
    return render(request, 'main/stat_wtime.html', context)

# Соотношение мужчин и женщин
@login_required
def show_stat_sex(request):
    res = Employee.objects.aggregate(min_date=Min('empdate'))
    c_year = date.today().year
    yr = c_year
    years = range(c_year, res['min_date'].year - 1, -1)
    if request.method == 'POST':
        yr = int(request.POST['year'])

    s_date = date(yr, 12, 31)
    d_cond = Q(empdate__lt=s_date) & \
        ( Q(dismdate__isnull=True) | Q(dismdate__gt=s_date) )
    m_cond = Q(sex='m') & d_cond
    f_cond = Q(sex='f') & d_cond
    m_cnt = Employee.objects.filter(m_cond).count()
    f_cnt = Employee.objects.filter(f_cond).count()
    context = { 'm': m_cnt, 'f': f_cnt, 'years': years, 'year': yr }
    return render(request, 'main/stat_sex.html', context)

# Прием на работу по годам
@login_required
def show_stat_emp(request):
    res = Employee.objects.aggregate(min_date=Min('empdate'))
    min_year = res['min_date'].year
    max_year = date.today().year
    years = range(min_year, max_year + 1, 1)

    deps = Department.objects.all()
    c_dep = -1
    if request.method == 'POST':
        c_dep = int(request.POST['dep'])

    if c_dep >= 0:
        dep_cond = Q(department=c_dep)
    else:
        dep_cond = Q(department__isnull=False)

    emps = []
    for y in years:
        min_date = date(y, 1, 1)
        max_date = date(y, 12, 31)
        d_cond = Q(empdate__lte=max_date) & Q(empdate__gte=min_date) & dep_cond
        n = Employee.objects.filter(d_cond).count()
        emps.append(n)

    context = { 'years': years, 'emps': emps, 'deps': deps, 'c_dep': c_dep }
    return render(request, 'main/stat_emp.html', context)

# Увольнения
@login_required
def show_stat_dism(request):
    res = Employee.objects.aggregate(min_date=Min('empdate'))
    min_year = res['min_date'].year
    max_year = date.today().year
    years = range(min_year, max_year + 1, 1)

    deps = Department.objects.all()
    c_dep = -1
    if request.method == 'POST':
        c_dep = int(request.POST['dep'])

    if c_dep >= 0:
        dep_cond = Q(department=c_dep)
    else:
        dep_cond = Q(department__isnull=False)

    disms = []
    for y in years:
        min_date = date(y, 1, 1)
        max_date = date(y, 12, 31)
        d_cond = Q(dismdate__isnull=False) & Q(dismdate__lte=max_date) & \
            Q(dismdate__gte=min_date) & dep_cond
        n = Employee.objects.filter(d_cond).count()
        disms.append(n)

    context = { 'years': years, 'disms': disms, 'deps': deps, 'c_dep': c_dep }
    return render(request, 'main/stat_dism.html', context)

# Отпуска помесячно
@login_required
def show_stat_vac(request):
    res = Vacation.objects.aggregate(min_date=Min('startdate'))
    min_year = res['min_date'].year
    max_year = date.today().year
    years = range(max_year, min_year - 1, -1)

    yr = max_year
    if request.method == 'POST':
        yr = int(request.POST['year'])

    vacs = []
    for i in range(1, 13):
        s_date = date(yr, i, 1)
        if i == 12:
            e_date = date(yr + 1, i, 1)
        else:
            e_date = date(yr, i + 1, 1)
        d_cond = Q(startdate__gte=s_date) & \
            Q(startdate__lt=e_date)
        n = Vacation.objects.filter(d_cond).count()
        vacs.append(n)

    context = { 'vacs': vacs, 'years': years, 'year': yr }
    return render(request, 'main/stat_vac.html', context)

# Возрастные категории
@login_required
def show_stat_age(request):
    nd = date.today()

    deps = Department.objects.all()
    c_dep = -1
    if request.method == 'POST':
        c_dep = int(request.POST['dep'])

    if c_dep >= 0:
        dep_cond = Q(department=c_dep)
    else:
        dep_cond = Q(department__isnull=False)

    # 18-25, 25-40, 40-55, 55+
    age_list = [18, 25, 40, 55, 200]
    ages = []
    for i in range(0, 4):
        min_date = nd - timedelta(365 * age_list[i + 1])
        max_date = nd - timedelta(365 * age_list[i])
        d_cond = Q(birthday__lte=max_date) & \
            Q(birthday__gt=min_date)

        # Не показывать уволенных сотрудников
        c_emp = Q(dismdate__isnull=True)
        n = Employee.objects.filter(d_cond & dep_cond & c_emp).count()
        ages.append(n)

    context = { 'ages': ages, 'deps': deps, 'c_dep': c_dep }
    return render(request, 'main/stat_age.html', context)

from django.db import models

# Средняя зарплата по отделам
@login_required
def show_stat_saldep(request):
    # deps = Department.objects.annotate(ave=Avg('employee__salary', output_field=models.FloatField()))
    deps = Department.objects.all()
    context = { 'deps': deps }
    return render(request, 'main/stat_saldep.html', context)

# Средняя зарплата по должностям
@login_required
def show_stat_salpos(request):
    # posts = Post.objects.annotate(ave=Avg('employee__salary', output_field=models.FloatField()))
    # context = { 'posts': posts }
    deps = Department.objects.all()
    c_dep = -1
    if request.method == 'POST':
        c_dep = int(request.POST['dep'])

    Post.dep = c_dep

    if c_dep >= 0:
        raw = Post.objects.filter(staff__department=c_dep)
    else:
        raw = Post.objects.all()

    posts = raw
    context = { 'posts': posts, 'deps': deps, 'c_dep': c_dep }
    return render(request, 'main/stat_salpos.html', context)

# Наличие высшего образования
@login_required
def show_stat_edu(request):
    res = Employee.objects.aggregate(min_date=Min('empdate'))
    c_year = date.today().year
    yr = c_year
    years = range(c_year, res['min_date'].year - 1, -1)
    if request.method == 'POST':
        yr = int(request.POST['year'])

    s_date = date(yr, 12, 31)
    d_cond = Q(empdate__lt=s_date) & \
        ( Q(dismdate__isnull=True) | Q(dismdate__gt=s_date) )
    e_cond = Q(diploma__dtype__icontains='высшее')
    edu_y = Employee.objects.filter(d_cond & e_cond).distinct().count()
    edu_n = Employee.objects.filter(d_cond).count() - edu_y
    # a = Employee.objects.filter(d_cond & e_cond).distinct()
    # b = Employee.objects.filter(d_cond)
    context = { 'edu_y': edu_y, 'edu_n': edu_n, 'years': years, 'year': yr
        # , 'a': a, 'b': b 
        }
    return render(request, 'main/stat_edu.html', context)

# -------------------- "Аналитика" --------------------
@login_required
def showana(request):
    return HttpResponseRedirect(reverse('showanaexp'))

# Прогноз расходов на зарплату по отделам
@login_required
def show_ana_exp(request):
    res = {}
    # Цикл по отделам
    deps = Department.objects.all()
    for dep in deps:
        n_workers = Employee.objects.filter(department=dep.pk).count()
        n_all = n_workers
        lst_year = []
        lst_exp = []
        sals = Salary.objects.filter(department=dep.pk).order_by('year')
        for sal in sals:
            lst_year.append(sal.year)
            lst_exp.append(sal.exp)
        
        prop = 0.0
        k = 1.0
        for i in range(len(lst_year) - 1, 1, -1):
            prop += ( (lst_exp[i] - lst_exp[i-1]) * k * 2.0 / 3.0 )
            k = k / 3.0
        prop += (lst_exp[1] - lst_exp[0]) * k
        prop += lst_exp[-1]

        delta = 0.0
        wplaces = Staff.objects.filter(department=dep.pk)
        for pos in wplaces:
            pst = Post.objects.get(pk=pos.post.pk)
            n_all += (pos.num - pos.workers())
            delta += (pos.num - pos.workers()) * (pst.salarymin + pst.salarymax) / 2.0
        
        if n_all > 0:
            prop = (prop * n_workers + delta) / n_all
        lst_exp.append(prop)
        lst_exp.append( (lst_exp[-1] - lst_exp[-2]) / lst_exp[-2] * 100.0 )
        lst_exp.append( dep.imp )
        res[dep.title] = lst_exp[-4::]

    lst_k = []
    lst_nk = []
    for dep in res:
        if res[dep][3]:
            lst_k.append([ dep, res[dep][2] ])
        else:
            lst_nk.append([ dep, res[dep][2] ])
    lst_k = sorted(lst_k, key=lambda item: item[1], reverse=True)

    flag = False
    depart = ''
    for k_dep in lst_nk:
        if len(lst_k) > 0 and int(k_dep[1]) > int(lst_k[0][1]):
            if flag:
                depart += ', '
            depart += f'"{k_dep[0]}"'
            flag = True

    context = {'deps': res, 'flag': flag, 'depart': depart}
    return render(request, 'main/ana_exp.html', context)

# Прогноз увольнений сотрудников
@login_required
def show_ana_dism(request):
    # Количество увольнений в каждом месяце
    mons = {}
    # Средний стаж до увольнения в каждом отделе
    deps = {}
    # Средний возраст при увольнении в каждом отделе
    ages = {}

    # Цикл по уволенным работникам
    emps = Employee.objects.filter(dismdate__isnull=False)
    for emp in emps:
        mons.setdefault(emp.dismdate.month, 0)
        mons[emp.dismdate.month] += 1

        # Вычисления суммарного стажа (до увольнения) по отделам
        deps.setdefault(emp.deppost(), [timedelta(), 0.0])
        deps[emp.deppost()][0] += (emp.dismdate - emp.empdate)
        deps[emp.deppost()][1] += 1.0

        # Вычисление суммарного возраста при увольнении
        ages.setdefault(emp.deppost(), timedelta())
        ages[emp.deppost()] += (emp.dismdate - emp.birthday)

    # Вычисление среднего стажа (до увольнения) и возраста по отделам
    for dep in deps:
        ages[dep] = ages[dep] / deps[dep][1]
        deps[dep] = deps[dep][0] / deps[dep][1]
        
        
    # Упорядочиваем месяцы по количеству увольнений в обратном порядке
    m_tup = sorted(mons.items(), key=lambda item: item[1], reverse=True)
    m_tup = m_tup[:3:]          # Оставляем не больше 3-х месяцев
    mons = {k : v for k, v in m_tup}
    if 12 not in mons:          # Добавляем в словарь последний месяц года
        mons[12] = 0

    mons_titles = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 
        'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    emps_data = {}
    # Просматриваем всех работающих сотрудников
    emps = Employee.objects.filter(dismdate__isnull=True)
    for emp in emps:
        if emp.deppost() not in deps:
            continue
        
        # Проверяем, соответствует ли образование сотрудника образованию увольнявшихся
        # работников
        # e_set = Employee.objects.filter(department=emp.department, dismdate__isnull=False)
        # n_edu = 0
        # for e in e_set:
        #     a = Diploma.objects.filter(employee=emp.pk)
        #     b = Diploma.objects.filter(employee=e.pk)
        #     if a.first() is None or b.first() is None:
        #         continue
        #     if a.first().dtype == b.first().dtype:
        #         n_edu += 1
        # if n_edu / e_set.count() < 0.5:
        #     continue

        for mon in mons:
            curr_d = date(date.today().year + 1, mon, 28)
            # Вычисляем возраст сотрудника на дату увольнения
            age = curr_d - emp.birthday
            if age < ages[emp.deppost()] - timedelta(days=365 * 3) or \
                age > ages[emp.deppost()] + timedelta(days=365 * 3):
                continue
            if emp.empdate + deps[emp.deppost()] < curr_d:
                # Сохраняем данные работника и месяц
                emps_data[emp.pk] = [0, 0, 0, 0, 0, 0]
                emps_data[emp.pk][0] = emp.pnumber
                emps_data[emp.pk][1] = emp.__str__()
                emps_data[emp.pk][2] = emp.department.title
                emps_data[emp.pk][3] = emp.post.title
                emps_data[emp.pk][4] = str(mons_titles[mon - 1]) + ', ' + str(date.today().year + 1)

    context = {'mons': mons, 'emps': emps_data, 'ages': ages, 'deps': deps}
    return render(request, 'main/ana_dism.html', context)


from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Создание потомка LogoutView для указания альтернативного
# шаблона страницы выхода
class PerfLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logout.html'
