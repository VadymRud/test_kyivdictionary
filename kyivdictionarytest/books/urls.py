from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)