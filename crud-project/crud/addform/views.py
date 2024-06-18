from django.shortcuts import render
from addform.forms import Studentregistration
from addform.models import User
from django.http import HttpResponseRedirect
# Create your views here.
def add(request):
  if request.method=='POST':
    fm=Studentregistration(request.POST)
    if fm.is_valid():
      nm=fm.cleaned_data['name']
      mail=fm.cleaned_data['email']
      pss=fm.cleaned_data['password']
      reg=User(name=nm,email=mail,password=pss)
      reg.save()
      fm=Studentregistration()
  else: 
      fm=Studentregistration()
  info=User.objects.all()
  return render(request,'addformtemp/addandshow.html',{'form':fm,'show':info})

def delete(request,id):
  if request.method=='POST':
    dl=User.objects.get(pk=id)
    dl.delete()
  return HttpResponseRedirect('/')
def edit(request,id):
  if request.method=='POST':
    ed=User.objects.get(pk=id)
    fm=Studentregistration(request.POST,instance=ed)
    if fm.is_valid():
      fm.save()
  else:
    ed=User.objects.get(pk=id)
    fm=Studentregistration()
  return render(request,'addformtemp/update.html',{'form':fm})