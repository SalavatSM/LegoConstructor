from django.db import models


class Block(models.Model):
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
    ]

    shape = models.CharField(max_length=100)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    size = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.shape} {self.color} {self.size}'


class Set(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    blocks = models.ManyToManyField(Block)

    def __str__(self):
        return self.name


