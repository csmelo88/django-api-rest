from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Usuario(Base):
    nome = models.CharField(max_length=100)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'nome'

    def __str__(self):
        return self.nome

class Dados(Base):
    usuario = models.ForeignKey(Usuario, related_name="Usuarios", on_delete=models.CASCADE)
    email = models.EmailField()
    contato = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Dado"
        verbose_name_plural = "Dados"
        unique_together = ['usuario', 'email']

    def __str__(self):
        return f'{self.usuario} email: {self.email} contato: {self.contato}'

