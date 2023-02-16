from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'item-detail',
            kwargs={'object_id': self.id}
        )


class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    caption = models.CharField(
        max_length=250, blank=True
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'photo-detail',
            kwargs={'object_id': self.id}
        )
