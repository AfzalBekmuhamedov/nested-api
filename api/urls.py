from django.urls import path

from api.views import *

urlpatterns = [
    path("category/",CategoryView.as_view(),name="category"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category2"),
    path("subcategory/", SubCategoryView.as_view(), name="subcategory"),
    path("subcategory/<int:pk>/", SubCategoryDetail.as_view(), name="subcategory"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("catalog/<int:pk>/", CatalogDetail.as_view(), name="catalog"),
]