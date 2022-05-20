# Маршруты приложения
from django.urls import path

from .views import index
from .views import showposts, addpost, editpost, delpost
from .views import showdeps, adddep, editdep, deldep
from .views import showemps, addemp, editemp, delemp, showdisms
from .views import adddip, editdip, deldip
from .views import addvac, editvac, delvac
from .views import addprom, editprom, delprom
from .views import showstaff, addstaff, editstaff, delstaff
from .views import showvacs, add2vac, edit2vac, del2vac
from .views import showproms, add2prom, edit2prom, del2prom
from .views import showstat
from .views import show_stat_pens, show_stat_wtime
from .views import show_stat_sex
from .views import show_stat_emp
from .views import show_stat_dism
from .views import show_stat_vac
from .views import show_stat_age
from .views import show_stat_saldep
from .views import show_stat_salpos
from .views import show_stat_edu
from .views import showana, show_ana_exp, show_ana_dism

urlpatterns = [
    # Post
    path('posts/', showposts, name='showposts'),
    path('addpost/', addpost, name='addpost'),
    path('editpost<int:post_id>/', editpost, name='editpost'),
    path('delpost<int:post_id>/', delpost, name='delpost'),

    # Department
    path('deps/', showdeps, name='showdeps'),
    path('adddep/', adddep, name='adddep'),
    path('editdep<int:dep_id>/', editdep, name='editdep'),
    path('deldep<int:dep_id>/', deldep, name='deldep'),

    # Employee
    path('emps/', showemps, name='showemps'),
    path('disms/', showdisms, name='showdisms'),
    path('addemp/', addemp, name='addemp'),
    path('editemp<int:emp_id>/', editemp, name='editemp'),
    path('delemp<int:emp_id>/', delemp, name='delemp'),

    # Diploma
    # path('dips/', showposts, name='showposts'),
    path('adddip<int:emp_id>/', adddip, name='adddip'),
    path('editdip<int:dip_id>/', editdip, name='editdip'),
    path('deldip<int:dip_id>/', deldip, name='deldip'),

    # Vacation
    path('addvac<int:emp_id>/', addvac, name='addvac'),
    path('editvac<int:vac_id>/', editvac, name='editvac'),
    path('delvac<int:vac_id>/', delvac, name='delvac'),

    path('vacs/', showvacs, name='showvacs'),
    path('add2vac/', add2vac, name='add2vac'),
    path('edit2vac<int:vac_id>/', edit2vac, name='edit2vac'),
    path('del2vac<int:vac_id>/', del2vac, name='del2vac'),

    # Promotion
    path('addprom<int:emp_id>/', addprom, name='addprom'),
    path('editprom<int:prom_id>/', editprom, name='editprom'),
    path('delprom<int:prom_id>/', delprom, name='delprom'),

    path('proms/', showproms, name='showproms'),
    path('add2prom/', add2prom, name='add2prom'),
    path('edit2prom<int:prom_id>/', edit2prom, name='edit2prom'),
    path('del2prom<int:prom_id>/', del2prom, name='del2prom'),

    # Staff
    path('staff/', showstaff, name='showstaff'),
    path('addstaff/', addstaff, name='addstaff'),
    path('editstaff<int:staff_id>/', editstaff, name='editstaff'),
    path('delstaff<int:staff_id>/', delstaff, name='delstaff'),

    # Statistic
    path('statpens/', show_stat_pens, name='showstatpens'),
    path('statwtime/', show_stat_wtime, name='showstatwtime'),
    path('statsex/', show_stat_sex, name='showstatsex'),
    path('statemp/', show_stat_emp, name='showstatemp'),
    path('statdism/', show_stat_dism, name='showstatdism'),
    path('statvac/', show_stat_vac, name='showstatvac'),
    path('statage/', show_stat_age, name='showstatage'),
    path('statsaldep/', show_stat_saldep, name='showstatsaldep'),
    path('statsalpos/', show_stat_salpos, name='showstatsalpos'),
    path('statedu/', show_stat_edu, name='showstatedu'),
    path('stat/', showstat, name='showstat'),

    # Analytics
    path('anaexp/', show_ana_exp, name='showanaexp'),
    path('anadism/', show_ana_dism, name='showanadism'),
    path('ana/', showana, name='showana'),

    # /
    path('', index, name='index'),
]