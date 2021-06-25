from django.db import models

# Create your models here.

class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

