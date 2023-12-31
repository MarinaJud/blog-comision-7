from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PublicarForm

# views basada en funcion para enlistar las publicaciones
"""
def publicaciones_view(request):
    ctx = {
        'publicaciones' : Publicacion.objects.all(),
    }
    return render(request, 'publicaciones.html', ctx)
"""

#view basada en clase para enlistar las publicaciones

class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'


#view basada en funcion para crear una publicacion
'''
def publicar_view(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save()
            return redirect('publicaciones')
    else:
        form = PublicarForm()
        ctx =  {'form': form}
        return render(request, 'publicaciones/publicar.html', ctx)
    
'''
#view basada en una clase para CREAR una publicacion
class Publicar(CreateView):
    model = Publicacion
    template_name= 'publicaciones/publicar.html'
    form_class = PublicarForm


 #view basada en una clase para MODIFICAR una publicacion

class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones'


