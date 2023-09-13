from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def business(request):
    return render(request, "for_business.html")


def talents(request):
    return render(request, "talents.html")


def our_solution(request):
    return render(request, "our_solutions.html")


def why_we_exist(request):
    return render(request, "why_we_exist.html")
