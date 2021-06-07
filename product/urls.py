from django.urls import path
from product import views

urlpatterns = [
    path('create/', views.ProductCreateView.as_view()),
    path('update/<pk>/', views.ProductUpdateView.as_view()),
    path('list/', views.ProductListView.as_view()),
    path('image/delete/<pk>/', views.ProductImageDeleteView.as_view()),
    path('image/upload/', views.ProductImageCreateView.as_view()),
    path('search/', views.ProductSearchByTagView.as_view()),

]