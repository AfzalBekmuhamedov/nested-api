from rest_framework import serializers
from .models import *

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ["id","name","image","subcategory"]

class SubCategorySerializer(serializers.ModelSerializer):
    catalogs = CatalogSerializer(many=True,read_only=True)
    class Meta:
        model = SubCategory
        fields = ["id","name","category","catalogs"]



class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ["id","title","subcategories"]



