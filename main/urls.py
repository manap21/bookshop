from django.urls import path

from .views import index, book_list

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', book_list, name='book-list'),
]