from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    category = models.CharField(max_length=300, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category': self.category,
        }


class Category(models.Model):
    name = models.CharField(max_length=300, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }