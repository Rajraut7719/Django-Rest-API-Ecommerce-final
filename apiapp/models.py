from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=225)

    class Meta:
        verbose_name_plural='categories'

    
    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=225,primary_key=True)
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    author=models.CharField(max_length=200,default='Raj')
    isbn=models.CharField(max_length=13)
    pages=models.IntegerField()
    price=models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    imgeUrl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_created']

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    price=models.IntegerField()
    stock=models.IntegerField()
    imgeUrl=models.URLField()
    status=models.BooleanField(default=True)
    date_created=models.DateField(auto_now_add=True)

    class Meta:
         ordering=['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)




