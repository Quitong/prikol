from django.db import models



class Category(models.Model):
    name = {}


class Goods(models.Model):
    name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', models.CASCADE)