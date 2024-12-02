from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# or from .models import Course


# Create your views here.

def index(request):
    courses = Course.objects.all()
    c = str(datetime.now())
    return render(request, 'courses.html', {'courses': courses})

def single_course(request, course_id):
    course = Course.objects.get(pk = course_id)
    return render(request, 'single_course.html', {'course': course} )