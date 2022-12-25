from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import ConteudoForm

def index(request):
    conteudo = Tarefa.objects.all()
    form = ConteudoForm()
    if request.method=='POST':
        form= ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/')

    context = {
        'conteudos':conteudo,
        'form':form
    }
    return render(request,'lista.html', context)

def delete_tarefa(request,id):
    delete = Tarefa.objects.get(id=id)
    delete.delete()
    return redirect('/')

