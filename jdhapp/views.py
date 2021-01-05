from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import InstructorCreate, StudentCreate
from .models import Student, Course


def index(request):
    return render(request, "index.html")


def InstructorCreateView(request):
    context = {}

    form = InstructorCreate(request.POST or None)
    if form.is_valid():
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                        is_staff=True)
        Group.objects.get(name='instructor').user_set.add(user)
        user.save()
        form.save()
        return HttpResponseRedirect('/instructor')

    context['form'] = form
    return render(request, "instructor.html", context)


def StudentCreateView(request):
    context = {}

    form = StudentCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/studentlogin')

    context['form'] = form
    return render(request, "student.html", context)


def StudentLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if Student.objects.filter(username=username, password=password).exists():
            context = {"allcourses": Course.objects.all()}
            response = render(request, "courses.html", context)
            return response
        else:
            content = {'error': "INVALID USERNAME/PASSWORD"}
            return render(request, "studentlogin.html", content)
    return render(request, "studentlogin.html")


def StudentLogout(request):
    return render(request, "studentlogin.html")


def courses(request):
    return render(request, "courses.html")
