from django.shortcuts import render
from django.http import JsonResponse

from Apps.students.models import StudentModel


def studentsView(request):
    students=StudentModel.objects.all() # As a Queryset (dictionary)
    #print(students.values()) #Query set list dictionary
    values_list=list(students.values()) # QuerySet is represent in list and inner its dictionary
    #print(values_list)
    return JsonResponse(values_list,safe=False) #JsonResponse always need to dictionary. safe=False means data should be comes any format
