from django.shortcuts import render, redirect
from .models import Equipments
from.forms import EquipmentsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def my_equipments(request):
    equipment = Equipments.objects.all()
    return render(request, 'equipment/equipments.html', {'equipment': equipment})


class EquipmentsDetailView(DetailView):
    model = Equipments
    template_name = 'equipment/details_view.html'
    context_object_name = 'equipment'


class EquipmentsUpdateView(UpdateView):
    model = Equipments
    template_name = 'equipment/create_equipment.html'

    form_class = EquipmentsForm


class EquipmentsDeleteView(DeleteView):
    model = Equipments
    success_url = '/equipment/'
    template_name = 'equipment/delete_equipment.html'


def create_equipment(request):
    error = ''
    if request.method == 'POST':
        form = EquipmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment')
        else:
            error = 'Форма заполнена не верно'

    form = EquipmentsForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'equipment/create_equipment.html', data)
