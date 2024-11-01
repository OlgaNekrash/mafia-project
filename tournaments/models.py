from django.db import models
from django.core.exceptions import ValidationError
from clubs.models import Club


class Tournament(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название турнира")
    date = models.DateField(verbose_name="Дата турнира")
    description = models.TextField(verbose_name="Описание турнира")
    image = models.ImageField(upload_to='tournament_images/', blank=True, null=True, verbose_name="Изображение турнира")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name="Клуб", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_info(self):
        return f"{self.name} - {self.date} - {self.description[:50]}..."


class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="Турнир")
    full_name = models.CharField(max_length=50, verbose_name="Полное имя")
    nickname = models.CharField(max_length=50, verbose_name="Никнейм")
    age = models.IntegerField(verbose_name="Возраст", blank=True, null=True)
    experience = models.FloatField(verbose_name="Опыт (лет)", blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    tg_link = models.CharField(max_length=40, verbose_name="Ссылка на Telegram")

    class Meta:
        unique_together = ('tournament', 'nickname')
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.nickname

    def clean(self):
        if self.age is not None and (self.age < 18 or self.age > 90):
            raise ValidationError('Возраст должен быть от 18 до 90 лет.')

        if self.experience is not None and (self.experience < 0.5 or self.experience > 40):
            raise ValidationError('Опыт должен быть от 0.5 до 40 лет.')

        if not all(c.isalpha() or c.isspace() for c in self.full_name):
            raise ValidationError('В полном имени могут быть только буквы и пробелы.')
