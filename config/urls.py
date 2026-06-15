from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.stocks.urls')),
    path('alerts/', include('apps.alerts.urls')),
]
