from django.urls import path
from .views import *

urlpatterns = [
    path('reviews/', ReviewViewSet.as_view({'get': 'list'})),
    path('reviews-picture/', ReviewPictureViewSet.as_view({'get': 'list'})),
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('books-picture/', BookPictureViewSet.as_view({'get': 'list'})),
    path('audio/', AudioFileViewSet.as_view({'get': 'list'})),
]
