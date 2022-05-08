from django.urls import path, include

from product import views as product_views

urlpatterns = [
    path('latest-products/', product_views.LatestProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', product_views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', product_views.CategoryDetail.as_view()),
    path('products/search', product_views.Search.as_view()),

]