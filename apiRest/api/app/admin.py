from django.contrib import admin
from .models import Base, Usuario, Dados

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'contato')
