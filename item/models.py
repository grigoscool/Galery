from django.db import models
from django.urls import reverse
from django.utils.text import slugify


from .fields import ImageRestrictedFileField


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
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    image = ImageRestrictedFileField(
        upload_to='photos', max_upload_size=524288,
        blank=True, null=True,
    )
    caption = models.CharField(
        max_length=250, blank=True
    )
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'photo-detail',
            kwargs={'object_id': self.id}
        )

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
