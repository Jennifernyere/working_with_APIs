from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class Link(models.Model):

    target = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass 

    def __str__(self):
        return self.title
    
    