from django.contrib import admin
from django.urls import path
from books.views import home, create_books
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create_books)
]
