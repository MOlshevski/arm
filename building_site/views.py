from django.shortcuts import render, redirect
from .models import Sites
from.forms import SitesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def my_sites(request):
    sites = Sites.objects.all()
    return render(request, 'building_site/sites.html', {'sites': sites})


class SitesDetailView(DetailView):
    model = Sites
    template_name = 'building_site/details_view.html'
    context_object_name = 'building_sites'


class SitesUpdateView(UpdateView):
    model = Sites
    template_name = 'building_site/create_site.html'

    form_class = SitesForm


class SitesDeleteView(DeleteView):
    model = Sites
    success_url = '/building_sites/'
    template_name = 'building_site/delete_site.html'


class SitesDestinationView(DeleteView):
    model = Sites
    success_url = '/building_sites/'
    template_name = 'building_site/site_destination.html'


def create_site(request):
    error = ''
    if request.method == 'POST':
        form = SitesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sites')
        else:
            error = 'Форма заполнена не верно'

    form = SitesForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'building_site/create_site.html', data)
