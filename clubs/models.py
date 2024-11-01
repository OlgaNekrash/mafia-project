from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    photo = models.ImageField(upload_to='club_photos/',
                              default='club_photos/default.jpg')

    def __str__(self):
        return self.name
