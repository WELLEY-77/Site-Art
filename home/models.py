from django.db import models
from datetime import datetime

class GalleryArt(models.Model):
    title = models.CharField('Titulo', max_length=100)
    date_create = models.DateField('Data da Criação', auto_now=False, auto_now_add=False)
    details = models.CharField('Detalhes', max_length=300)
    photo_art = models.ImageField('Foto da Obra', upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self) :
        return f'{ self.title }'
    
