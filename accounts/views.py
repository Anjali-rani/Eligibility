from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    user_form=forms.UserForm()
    student_form=forms.StudentForm()
    mydict={'user_form': user_form,'student_form':student_form}
    if request.method=='POST':
        user_form=forms.UserForm(request.POST)
        student_form=forms.StudentForm(request.POST)
        if user_form.is_valid() and  student_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            stud=student_form.save(commit=False)
            stud.user=user

            stud=stud.save()
            my_student_group = Group.objects.get_or_create(name='Student')
            my_student_group[0].user_set.add(user)

        return HttpResponseRedirect('Studentlogin')

    return render(request,'accounts/register.html',context=mydict)


def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'accounts/adminsignup.html',{'form':form})


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_student(user):
    return user.groups.filter(name='Student').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin_dashboard')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):

    student=models.Student.objects.all().order_by('-id')
    mydict = {

        'student': student
             },
    return render(request, 'accounts/admin_dashboard.html', context=mydict)