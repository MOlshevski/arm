from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_sites, name='sites'),
    path('create_site', views.create_site, name='create_site'),
    path('<int:pk>', views.SitesDeleteView.as_view(), name='sites-detail'),
    path('<int:pk>/destination', views.SitesDestinationView.as_view(), name='site_destination'),
    path('<int:pk>/update', views.SitesUpdateView.as_view(), name='sites-update'),
    path('<int:pk>/delete', views.SitesDeleteView.as_view(), name='sites-delete'),
    ]