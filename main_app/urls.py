from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'), 
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'), 
    path('cat/<int:pk>/update', views.CatUpdate.as_view(), name='cat-update'),
    path('cat/<int:pk>/delete', views.CatDelete.as_view(), name='cat-delete')
]