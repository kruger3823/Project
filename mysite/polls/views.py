from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect,reverse
from .import models
from .forms import UserForm, Form, Medform
from .models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test



# Create your views here.






def registerUserpage(request):
    userForm= UserForm()
    userForm1= Form()
    mydict={'userForm':userForm,'userForm1':userForm1}
    if request.method=='POST':
        userForm= UserForm(request.POST)
        userForm1= Form(request.POST, request.FILES)
        if userForm.is_valid() and userForm1.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            print(user)
            doctor=userForm1.save(commit=True)
            doctor.user=user
            doctor.save()
            print(doctor)
            group = Group.objects.get_or_create(name='STUDENT')
            group[0].user_set.add(user)
        return redirect('login')
    return render(request,'sighnup.html',context=mydict)


def is_doctor(user):
    return user.groups.filter(name='STUDENT').exists()


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()




def afterlogin_view(request):
    if is_doctor(request.user):

        return redirect('dash')
    elif is_admin(request.user):
        return redirect('dashteacher')



@login_required(login_url='login')
@user_passes_test(is_doctor)
def dash(request):

    return render(request,'dash.html')

def dashteacher(request):

    return render(request,'dashteacher.html')


def course(request):
    return render(request,'courses.html',{'a':a},)



def bcaattendance(request):
    a=models.SEM1.objects.all().filter(sem=1,branch='bca')
    return render(request,'bcaattendance.html',{'a':a},)

def bscattendance(request):
    a = models.objects.all.filter(sem=1, branch='bsc')

    return render(request,'bscattendance.html',{'a':a},)


def logout_request(request):
	logout(request)
	return redirect("login")


def bcacourse(request):
    sem1 = models.tableinfo.objects.all().filter(semester=1,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)

def bcacourse2(request):
    sem1 = models.tableinfo.objects.all().filter(semester=2,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)

def bcacourse3(request):
    sem1 = models.tableinfo.objects.all().filter(semester=3,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)
def bcacourse4(request):
    sem1 = models.tableinfo.objects.all().filter(semester=4,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)
def bcacourse5(request):
    sem1 = models.tableinfo.objects.all().filter(semester=5,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)
def bcacourse6(request):
    sem1 = models.tableinfo.objects.all().filter(semester=6,user__id=request.user.id)

    return render(request,'semester1.html',{'sem1':sem1},)

def home(request):
    sem1 = models.tableinfo.objects.all().filter(semester=1,user__id=request.user.id)
    return render(request,'home.html',{'sem1':sem1},)


def a(request):
    sem1 = models.A.objects.all().filter(user__id=request.user.id)
    return render(request,'A.html',{'sem1':sem1},)
def b(request):
    sem1 = models.B.objects.all().filter(semester=1,user__id=request.user.id)
    return render(request,'B.html',{'sem1':sem1},)
def c(request):
    sem1 = models.C.objects.all().filter(semester=1,user__id=request.user.id)
    return render(request,'C.html',{'sem1':sem1},)
def d(request):
    sem1 = models.D.objects.all().filter(semester=1,user__id=request.user.id)
    return render(request,'D.html',{'sem1':sem1},)
def e(request):
    sem1 = models.E.objects.all().filter(semester=1,user__id=request.user.id)
    return render(request,'E.html',{'sem1':sem1},)




















#------------------------------Subjects wise -----------------------------------#


def TRANSACTIONS(request):
    sem=models.TRANSACTIONS.objects.all()
    return render(request, 'sub.html', {'sem': sem}, )




#-------------------------------semwise attendance----------------------------------#

def attendance(request):
    return render(request, 'Attendance.html', {'a': a})



def seps1(request):
    a=models.SEM1.objects.filter(user=request.user,sem=1)
    for i in a:
        c=(((i.m1+i.m2+i.m3+i.m4+i.m5)*100)/500)

    return render(request, 'sem1attendance.html', {'a': a,'c':c} )















def evu(request):
    sem1 = models.tableinfo.objects.all().filter(user__id=request.user.id)

    evu = []
    for i in sem1:
        evu.append(i.total)


    if len(evu) > 0:
        a = 0
        for j in evu:
            a = a + j
            print(a)
        if a>250:
            b='Good'
        else:
            b='Bad'
        print(b)
        mydict={

            'a':a,'b':b

        }
        return render(request, 'evu.html',context=mydict)
    return render(request, 'evu.html')


'''@login_required(login_url='login')
@user_passes_test(is_doctor)
def doctor_edit_view1(request):
    doctor=Doctor.objects.get(user_id=request.user.id)
    user=User.objects.get(id=doctor.user_id)
    form1=DoctorUserForm(instance=doctor.user)
    form2=DoctorForm(request.FILES,instance=doctor)
    mydict={'form1':form1,'form2':form2,'doctor':doctor}
    if request.method=='POST':
        form1=DoctorUserForm(request.POST,instance=user)
        form2=DoctorForm(request.POST,instance=doctor)
        if form1.is_valid() and form2.is_valid():
            print(1)
            user=form1.save()
            user.set_password(user.password)
            user.save()
            form2.save()
            return redirect('doctordash')
    return render(request,'edit.html',mydict)'''


'''def doctor_edit_view(request):
    my_volunteer =Doctor.objects.get(user_id=request.user.id)
    #my_volunteer1 = Doctor.objects.filter(my_volunteer.gender)
    c=my_volunteer.mobile

    if request.method == "POST":
        my_volunteer = Doctor.objects.get(user_id=request.user)
        update_form = DoctorUserForm(request.POST, instance=my_volunteer.user)

        update_profile_form = DoctorForm(request.POST, instance=my_volunteer)

        if update_form.is_valid() and update_profile_form.is_valid():
            user=update_form.save()
            user.set_password(user.password)
            user.save()
            print(update_form)
            update_profile_form.save()
            messages.success(request, f'Your Account has been Updated')
            return redirect('doctordash')
    else:
        update_form = DoctorUserForm(instance=my_volunteer.user)
        update_profile_form = DoctorForm(instance=my_volunteer)
    context = {
        'update_form': update_form,
        'update_profile_form': update_profile_form,
        'c':c
    }
    return render(request, 'edit.html', context)


def med(request):

    doctor = Doctor.objects.get(user__id=request.user.id)

    form1 = Medform(instance=doctor.user)
    mydict = {'form1': form1,'doctor':doctor}

    if request.method == 'POST':

        form1 = Medform(request.POST)
        form1.user=request.user
        print(form1.user)
        if form1.is_valid():
            user1 = form1.save()
            #user1.mobile=form1.mobile
            user1.user=form1.user
            print(user1.user)
            user1.save()



    return render(request, 'med.html', mydict)'''