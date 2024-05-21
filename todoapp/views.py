from django.shortcuts import render,redirect
from todoapp.models import table

# Create your views here.
def home(request):
    data=table.objects.all()
    return render(request,"index.html",{"data":data})
def savedata(request):
    if request.method== "POST":
        title=request.POST.get('title')
        disc=request.POST.get('disc')   
        data=table(title=title,disc=disc)
        data.save()
        return redirect("home")
def updating(request,id):
    data=table.objects.get(id=id)
    if request.method== "POST":
        title=request.POST.get('utitle')
        disc=request.POST.get('udisc')   
        data.title=title
        data.disc=disc
        data.save()
        return redirect("home")
def delete(request,id):
    data=table.objects.get(id=id)
    data.delete()
    return redirect("home")
def update(request,id):
    data=table.objects.get(id=id)
    return render(request,"update.html",{'data':data})
