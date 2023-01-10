from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('plans/', include('plans.urls')),
    path('equipment/', include('equipment.urls')),
    path('workers/', include('workers.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


