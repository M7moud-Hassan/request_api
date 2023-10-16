from django.utils import timezone
from django.db import models

# Create your models here.


class ApiModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
    


class Headers(ApiModel):
    key = models.CharField(max_length=1000)
    value = models.CharField(max_length=1000)


class Body(ApiModel):
    key = models.CharField(max_length=1000)
    value = models.CharField(max_length=1000)


class Requests(ApiModel):
    url = models.CharField(max_length=1000)
    url_encript = models.CharField(max_length=1000)
    headers = models.ManyToManyField(Headers)
    bodies = models.ManyToManyField(Body)
