from django.shortcuts import render, redirect
from .models import Workers
from.forms import WorkersForm
from django.views.generic import DetailView, UpdateView, DeleteView


def my_workers(request):
    workers = Workers.objects.all()
    return render(request, 'workers/workers.html', {'workers': workers})


class WorkersDetailView(DetailView):
    model = Workers
    template_name = 'workers/details_view.html'
    context_object_name = 'worker'


class WorkersUpdateView(UpdateView):
    model = Workers
    template_name = 'workers/create_worker.html'

    form_class = WorkersForm


class WorkersDeleteView(DeleteView):
    model = Workers
    success_url = '/workers/'
    template_name = 'workers/delete_worker.html'


def create_worker(request):
    error = ''
    if request.method == 'POST':
        form = WorkersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workers')
        else:
            error = 'Форма заполнена не верно'

    form = WorkersForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'workers/create_worker.html', data)