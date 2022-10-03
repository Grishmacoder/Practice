from django.shortcuts import render
from django.http import HttpResponse
from.models import DataFirst


def home(request):
    context = {
        'data': DataFirst.objects.all()
    }
    return render(request, 'firstapplication/home.html', context)
def about(request):
    return render(request,'firstapplication/about.html',{'title': 'About'})