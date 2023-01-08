from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_workers, name='workers'),
    path('create_worker', views.create_worker, name='create_worker'),
    path('<int:pk>', views.WorkersDetailView.as_view(), name='workers-detail'),
    path('<int:pk>/update', views.WorkersUpdateView.as_view(), name='workers-update'),
    path('<int:pk>/delete', views.WorkersDeleteView.as_view(), name='workers-delete'),
    ]