from django.contrib import admin
from django.urls import include, path
from app import views
from accounts import views

from django.conf import settings

from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    
    path('app/params/', include('app_params.urls')),

    path('', include('app.urls')),

]


if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)