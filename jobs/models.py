from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(blank = True, max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def half_desc(self):
        desc = self.description[:200]

        return desc


class Review(models.Model):
    name = models.CharField(blank = True, max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
