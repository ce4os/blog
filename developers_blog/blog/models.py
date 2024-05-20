import markdown as md

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    
    # tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_at"]
