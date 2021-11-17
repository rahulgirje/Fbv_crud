from django import forms
from django.shortcuts import redirect, render
from .forms import LaptopModelForm
from .models import Laptop


def productview(request):
    template_name = 'firstapp/prods.html'
    laptop = Laptop.objects.all()
    context = {'laptop':laptop}
    return render(request, template_name, context )



def addview(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allprods')
    template_name = 'firstapp/addprod.html'
    context = {'form': form}
    return render(request, template_name, context)


def updateview(request, oid):
    obj = Laptop.objects.get(id = oid)
    form = LaptopModelForm(instance=obj)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('allprods')
    template_name = 'firstapp/addprod.html'
    context = {'form': form}
    return render(request, template_name, context)





def deleteview(request, i):
    obj = Laptop.objects.get(id = i)
    obj.delete()
    return redirect('allprods')
