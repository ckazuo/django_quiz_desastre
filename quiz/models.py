from django.db import models

# Create your models here.
class Questionario(models.Model):
    pergunta = models.CharField(max_length=200)
    alternativa1 = models.CharField(max_length=100) 
    alternativa2 = models.CharField(max_length=100) 
    alternativa3 = models.CharField(max_length=100) 
    alternativa4 = models.CharField(max_length=100) 
    resposta = models.CharField(max_length=64) 
    explica = models.CharField(max_length=200)
    imagem = models.CharField(max_length=200, default='sem imagem')

    def __str__(self):
        return f"{self.pergunta}: {self.resposta} {self.explica}"

class Ranking(models.Model):
    username = models.CharField(max_length=200)
    first = models.CharField(max_length=100) 
    last = models.CharField(max_length=100) 
    score = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.username}: {self.score}"