from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_equipments, name='equipment'),
    path('create_equipment', views.create_equipment, name='create_equipment'),
    path('<int:pk>', views.EquipmentsDetailView.as_view(), name='equipments-detail'),
    path('<int:pk>/update', views.EquipmentsUpdateView.as_view(), name='equipments-update'),
    path('<int:pk>/delete', views.EquipmentsDeleteView.as_view(), name='equipments-delete'),
    ]