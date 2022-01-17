from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image')
    tags = TaggableManager()

    def __str__(self):
        return self.title
