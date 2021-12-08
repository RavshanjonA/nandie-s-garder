from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    topping1 = models.CharField(max_length=64)
    topping2 = models.CharField(max_length=64)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
