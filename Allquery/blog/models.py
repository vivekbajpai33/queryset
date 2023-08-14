from django.db import models

class Date(models.Model):
    date = models.DateField()

 
class BaseIntro(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    song = models.CharField(max_length=200, null=True , blank=True)
    upload_by = models.CharField(max_length=100)

    class Meta:
        db_table = "title" 

    def __str__(self):
        return self.title

class RingTone(models.Model):
    time = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)
    intro = models.ManyToManyField(BaseIntro) 
    customer = models.FileField(upload_to='blog')


# Create your models here.
