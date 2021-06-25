from django.db import models

# Create your models here.

class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200)
    pub_date = models.DateTimeField(max_length = 100)
    body = models.TextField()

class QNA(models.Model):
    title = models.CharField(max_length=30)
    content_type = models.CharField(max_length=20)
    content = models.TextField()
    write_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

