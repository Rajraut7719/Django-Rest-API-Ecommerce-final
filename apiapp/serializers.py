from dataclasses import field, fields
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','title')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title','category','author','isbn','pages','price','stock','description','imgeUrl','status')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('product_tag','name','category','price','stock','imgeUrl','status','date_created')


