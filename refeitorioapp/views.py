from django.shortcuts import render, get_object_or_404,redirect
from refeitorioapp.forms import MesaForms
from refeitorioapp.models import Mesa



# Create your views here.
def index(request):
    mesas =Mesa.objects.all()
    return render(request, 'refeitorio/index.html',{'mesas':mesas})


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


def editar(request,id):
    mesa = get_object_or_404(Mesa, pk=id)
    form = MesaForms(instance=mesa)
    if request.method == "POST":
        form = MesaForms(request.POST, request.FILES,instance=mesa)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('mostrar')
        else:
            return render(request, 'refeitorio/editar.html', {'form': form,'mesa':mesa})
    else:
        return render(request, 'refeitorio/editar.html', {'form': form, 'mesa': mesa})


