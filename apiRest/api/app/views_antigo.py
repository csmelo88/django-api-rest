from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Dados
from .serializers import DadosSerializer, UsuarioSerializer

class UsuarioAPIView(APIView):
    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DadosAPIView(APIView):
    def get(self, request):
        dados = Dados.objects.all()
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DadosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)