from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from women_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.shop.urls')),
    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)