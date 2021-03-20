from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def home(request):
    if request.method=='POST' :     
        fm=StudentRegistration(request.POST )
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistration()  

    if request.method=='GET':
         fm=StudentRegistration() 

    return render(request,'addandshow.html',{'form':fm})


def showinfo(request):
    semp=User.objects.all()
    # print(semp)
    context={'semp': semp}
    return render(request, 'showinfo.html',context)


def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/showinfo')
            
def update(request,id):        
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration() 

    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)       

    return render(request,'updatestudent.html',{'form':fm})
    
