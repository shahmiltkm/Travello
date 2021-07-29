from django.shortcuts import render
from  travello.models import Destination

# Create your views here.
def register(request):
    

  
    dests= Destination.objects.all()

    return render(request,'register.html',{'dests':dests})