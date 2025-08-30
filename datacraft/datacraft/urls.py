from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls')),
    path('modeling/', include('apps.modeling.urls')),
    path('monitoring/', include('apps.monitoring.urls')),
    path('pipelines/', include('apps.pipelines.urls')),
    path('queries/', include('apps.queries.urls')),
    path('sources/', include('apps.sources.urls')),
    path('streaming/', include('apps.streaming.urls')),
    path('transformations/', include('apps.transformations.urls')),
]
