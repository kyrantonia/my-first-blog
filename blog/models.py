from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title=models.CharField("Título",max_length=200)
    text= models.TextField("Texto")
    created_date=models.DateTimeField(blank=True,null=True)
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
