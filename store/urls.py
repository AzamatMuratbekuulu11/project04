from django.urls import path
from .views import BookViewSets
from .views import AuthorViewSets


urlpatterns = [
    path('', BookViewSets.as_view({'get': 'list', 'post': 'create'}), name='book_list'),
    path('<int:pk>/', BookViewSets.as_view({'get': 'retrieve',
                                   'put': 'update',
                                   'delete': 'destroy'}), name='book_detail'),

    path('Author', AuthorViewSets.as_view({'get': 'list', 'post': 'create'}), name='author_list'),
    path('Author/<int:pk>/', AuthorViewSets.as_view({'get': 'retrieve',
                                   'put': 'update',
                                   'delete': 'destroy'}), name='author_detail'),
]