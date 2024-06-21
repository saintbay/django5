from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class Song(models.Model):
    class Genre(models.TextChoices):
        ROCK = ('rock', 'Рок')
        RAP = ('rap', 'Рэп')
        CLASSICAL = ('classical', 'Классика')
        JAZZ = ('jazz', 'Джаз')
        METAL = ('metal', 'Метал')
        POP = ('pop', 'Поп')
        OTHER = ('other', 'Другое')

    name = models.CharField(max_length=255, validators=[MinLengthValidator(4, "Длина должна быть более 4 символов.")])
    author = models.CharField(max_length=255, validators=[MinLengthValidator(4, "Длина должна быть более 4 символов.")])
    producer = models.CharField(max_length=255, validators=[MinLengthValidator(4, "Длина должна быть более 4 символов.")])
    genre = models.CharField(max_length=10, choices=Genre.choices)
    year = models.IntegerField(validators=[MinValueValidator(1890, "Не раньше 1890 года."), MaxValueValidator(2025, "Не позже 2025 года")])
    rating = models.IntegerField(validators=[MinValueValidator(0, 'Принимается только положительные числа и ноль')], null=True)