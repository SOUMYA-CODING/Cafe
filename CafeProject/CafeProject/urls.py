from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApps.urls')),
    path('food/', include('FoodApp.urls')),
    path('user/', include('UserApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
