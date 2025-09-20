from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dream_bridge_app.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    # Pour les médias
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Pour les statiques
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
