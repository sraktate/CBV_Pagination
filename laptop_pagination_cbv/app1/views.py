from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.views.generic import ListView

# Create your views here.

def Home_view(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)

def Laptop_add_view(request):
    form=LaptopModelForm()
    if request.method =='POST':
        form=LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name='laptopadd.html'
    context={'form':form}
    return render(request,template_name,context)

class LaptopListView(ListView):
    paginate_by = 1
    model = Laptop
    template_name='laptopshow.html'