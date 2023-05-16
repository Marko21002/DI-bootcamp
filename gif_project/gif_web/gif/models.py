from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}, {self.uploader_name}'
# name (CharField)
# gifs - (many-to-many field with the Gif Model). A Gif can have many different categories, and a category can be shared among many gifs


class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif)

    def __str__(self) -> str:
        return f'{self.name}'
