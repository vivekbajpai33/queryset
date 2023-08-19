from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
from .form import *
from .models import *



class Home(View):
    teamplate = 'blog/teamplate/blog.html'
    title = "Home"
    form = Blog

    def get(self,request):
        title = self.title
        return render(request,self.teamplate,{'di':title})
    
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,self.teamplate)
        return HttpResponseRedirect(self.teamplate)

class About(View):
    teamplate = 'blog/teamplate/about.html'
    title = "ABOUT"
    form = AboutForm   
    ourdata = RingTone.objects.all()


    def get(self,request):

        three = RingTone.objects.all()
        base = BaseIntro.objects.all()

        context = {
            'third':three,
            'base':base,
            'di':self.title,

        }
        return render(request,self.teamplate,context)
    
    def post(self,request):
        pass
        
        # date = request.POST.get('time')
        # intro = request.POST.get('intro')
        # file =  request.POST.get('customer')


    
    





# Create your views here.
