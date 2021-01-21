from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Author(models.Model):
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    image = models.FileField(blank = True, null= True,verbose_name="yazar Fotoğraf Ekleyin")
    filter = models.CharField(max_length = 50, verbose_name = "filtre")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

class Quotations(models.Model):
    artist = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    conten_quotations = RichTextField(verbose_name = "Alıntılar",  null=True, blank=True)
    
    def __str__(self):
        return self.conten_quotations

    class Meta:
        ordering = ['-id']

class Quotation(models.Model):
    artist = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    content = models.TextField(verbose_name = "Alıntı", null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']

