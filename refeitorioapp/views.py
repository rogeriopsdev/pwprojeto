from django.shortcuts import render
from refeitorioapp.forms import MesaForms

# Create your views here.
def index(request):
    return render(request,'refeitorio/index.html')

def criar_mesa(request):
    form = MesaForms()
    return render(request,'refeitorio/criar_mesa.html',{'form':form})

