from django.shortcuts import render,HttpResponse
from django.views import View



class Home(View):
    def get(self,request):
        return HttpResponse("hil")



# Create your views here.
