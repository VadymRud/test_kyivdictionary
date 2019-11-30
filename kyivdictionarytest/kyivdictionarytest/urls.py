from django.contrib import admin
from django.urls import path
from books.views import BookList, BookSearh, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('search/<str:string>/', BookSearh.as_view()),

    path('book/add/', BookCreate.as_view(), name='books-add'),
    path('book/<int:pk>/', BookUpdate.as_view(), name='books-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='books-delete'),
]
