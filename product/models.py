from django.db import models

class MainContents(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    pub_date=models.DateTimeField('date published')