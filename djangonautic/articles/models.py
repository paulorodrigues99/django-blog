from django.db import models
from django.contrib.auth.models import User

# class Convite(models.Model):
#     solicitante = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_feitos')
#     convidado = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='convites_recebidos')

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT ,default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
