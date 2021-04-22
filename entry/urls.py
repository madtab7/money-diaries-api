from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

router = routers.DefaultRouter()
router.register(r'^entries', views.EntryView, basename='entry')

urlpatterns = [
    url(r'^test/', views.index, name='index'),
    url(r'^schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema', template_name='api/swagger-ui.html'), name="docs"),
    path('', include(router.urls))

]