from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_plans, name='plans'),
    path('create_plan', views.create_plan, name='create_plan'),
    path('<int:pk>', views.PlansDetailView.as_view(), name='plans-detail'),
    path('<int:pk>/update', views.PlansUpdateView.as_view(), name='plans-update'),
    path('<int:pk>/delete', views.PlansDeleteView.as_view(), name='plans-delete'),
    ]
