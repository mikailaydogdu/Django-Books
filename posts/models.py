from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField()
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    article = models.ForeignKey(Posts,on_delete = models.CASCADE,verbose_name = "post",related_name="comments")
    comment_content = models.TextField(verbose_name = "Yorum")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-created_date']