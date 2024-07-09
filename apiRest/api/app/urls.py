from django.urls import path
from .views import UsuarioAPIView, DadosAPIView

urlpatterns = [
    path('usuarios/', UsuarioAPIView.as_view(), name='usuarios'),
    path('dados/', DadosAPIView.as_view(), name='dados')
]