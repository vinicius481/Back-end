from django.db import models

class  Fotografia(models.Model):

    Opcoes_Categoria= [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
        ("SATÉLITE NATURAL", "satélite natural"),

    ] 

    nome = models.CharField(max_length= 100, null = False, blank = False) # black e para não permite que exitas "" <== strings vazis
    legenda = models.CharField(max_length= 150, null = False, blank = False)
    categoria = models.CharField(max_length=100, choices= Opcoes_Categoria, default='')
    descricao = models.TextField(null = False, blank = False)
    foto = models.CharField(max_length= 100, null = False, blank = False)

    def __str__(self) :
        return f'Fotogradia [nome = {self.nome}]'