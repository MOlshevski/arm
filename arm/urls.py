from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from arm.main.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('plans/', include('plans.urls')),
    path('equipment/', include('equipment.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = pageNotFound
