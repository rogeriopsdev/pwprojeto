from django.shortcuts import render
from refeitorioapp.forms import MesaForms
from refeitorioapp.models import Mesa


# Create your views here.
def index(request):
    return render(request, 'refeitorio/index.html')


def criar_mesa(request):
    form = MesaForms(request.POST)
    if request.method == "POST":
        form = MesaForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form = MesaForms()
    return render(request, 'refeitorio/criar_mesa.html', {'form': form})


def mostrar(request):
    itens = Mesa.objects.all()
    return render(request,"refeitorio/mostrar.html",{'itens':itens})