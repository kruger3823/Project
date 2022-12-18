from django.contrib.auth.views import LoginView
from django.urls import path
from.import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.registerUserpage,name="registerUserpage"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('dash/',views.dash,name="dash"),
path('dashteacher/',views.dashteacher,name="dashteacher"),
    path('course/',views.course,name="course"),
path('bcattendance/',views.bcaattendance,name="bcaattendance"),
path('bscattendance/',views.bscattendance,name="bscattendance"),

path('home/',views.home,name="home"),
path('evu/',views.evu,name="evu"),


path('a/',views.a,name="a"),
path('b/',views.b,name="b"),
path('c/',views.c,name="c"),
path('d/',views.d,name="d"),
path('e/',views.e,name="e"),



    ##############
path('bcacourse/',views.bcacourse,name="bcacourse"),
path('bcacourse2/',views.bcacourse2,name="bcacourse2"),
path('bcacourse3/',views.bcacourse3,name="bcacourse3"),
path('bcacourse4/',views.bcacourse4,name="bcacourse4"),
path('bcacourse5/',views.bcacourse5,name="bcacourse5"),
path('bcacourse6/',views.bcacourse6,name="bcacourse6"),







################ subs ###################
path('TRANSACTIONS/',views.TRANSACTIONS,name="TRANSACTIONS"),





################ attendance ###################

path('attendance/',views.attendance,name="attendance"),
path('sep/',views.seps1,name="sep"),




#    path('doctor_edit_view/',views.doctor_edit_view,name="doctor_edit_view"),
#    path('med/',views.med,name="med"),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)