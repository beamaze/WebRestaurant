from django.db import models

# Create your models here.
class Category(models.Model):

    category_text = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_text

class Menu(models.Model):

    menu_text = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.menu_text

class MenuItem(models.Model):

    name_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menus = models.ManyToManyField(Menu)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name_text