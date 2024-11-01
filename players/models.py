from django.db import models
from clubs.models import Club


class Players(models.Model):
    nickname = models.CharField(max_length=50, verbose_name="Никнейм")
    experience = models.PositiveIntegerField(verbose_name="Опыт (в годах)")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")

    clubs = models.ManyToManyField(Club, blank=True, related_name='players', verbose_name="Клубы")

    def __str__(self):
        return self.nickname
