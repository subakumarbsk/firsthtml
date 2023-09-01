from django.shortcuts import render
from django.http import HttpResponse
from .models import urdata
# Create your views here.
def home(request):
    #if request.method=="GET":
        #name = request.GET['names']
        #number = request.GET["number"]
        #dob = request.GET["dob"]
        #obj = urdata()
        #obj.Name=name
        #obj.Number=number
        #obj.birth = dob
        #obj.save()
    return render(request,'page.html')
def formres(request):
    return HttpResponse("Successfully Submittes")