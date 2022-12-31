from django.shortcuts import render, redirect
from .models import Plans
from.forms import PlansForm
from django.views.generic import DetailView, UpdateView, DeleteView


def my_plans(request):
    plans = Plans.objects.all()
    return render(request, 'plans/plans.html', {'plans': plans})


class PlansDetailView(DetailView):
    model = Plans
    template_name = 'plans/details_view.html'
    context_object_name = 'plan'


class PlansUpdateView(UpdateView):
    model = Plans
    template_name = 'plans/create_plan.html'

    form_class = PlansForm


class PlansDeleteView(DeleteView):
    model = Plans
    success_url = '/plans/'
    template_name = 'plans/delete_plan.html'


def create_plan(request):
    error = ''
    if request.method == 'POST':
        form = PlansForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plans')
        else:
            error = 'Форма заполнена не верно'

    form = PlansForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'plans/create_plan.html', data)
