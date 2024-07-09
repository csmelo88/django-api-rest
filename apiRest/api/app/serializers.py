from rest_framework import serializers
from .models import Usuario, Dados

class DadosSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Dados
        fields = (
            'id',
            'email',
            'contato',
            'criacao',
            'ativo'
        )

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'id',
            'nome',
            'url',
            'criacao',
            'ativo'
        )