from django.db import models

class Tarefa(models.Model):
    conteudo = models.CharField(max_length=1000)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
