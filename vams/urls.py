from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio),
    path('servicios/', views.servicios),
    path('nosotros/', views.nosotros),
    path('aretes/', views.aretes_view),
    path('collares/', views.collares_view),
    path('iniciosesion/', views.ingresar),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

