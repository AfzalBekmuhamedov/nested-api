from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategories")

    def __str__(self):
        return self.name

class Catalog(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="catalogs")

    def __str__(self):
        return self.name