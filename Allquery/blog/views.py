from django.shortcuts import render,HttpResponse
from django.views import View
from .form import Blog



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
            return HttpResponse("Thanks")
        return HttpResponse("rrr")
    
    





# Create your views here.
