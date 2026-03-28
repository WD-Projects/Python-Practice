from django.db import models
class Blog(models.Model):
    title = models.CharField()
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)