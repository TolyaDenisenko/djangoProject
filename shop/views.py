from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course
# or from .models import Course


# Create your views here.

def index(request):
    courses = Course.objects.all()
    c = str(datetime.now())
    return render(request, 'shop/courses.html', {'courses': courses})

def single_course(request, course_id):
    # try:
    #  course = Course.objects.get(pk = course_id)
    #  return render(request, 'single_course.html', {'course': course} )
    # except Course.DoesNotExist:
    #     raise Http404()

    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course} )