from django.contrib import admin
from django.urls import path
from books.views import BookList

urlpatterns = [
    path('books/', BookList.as_view()),
    path('admin/', admin.site.urls),
]
