from django.contrib import admin
from blog.models import *


@admin.register(BaseIntro)
class BaseIntroAdmin(admin.ModelAdmin):
    list_display = ['id','title','song','upload_by']
    list_filter = ['title']

@admin.register(RingTone)
class RingToneAdmin(admin.ModelAdmin):
    list_display = ['id','time','customer']




# Register your models here.
