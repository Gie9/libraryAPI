from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


# Code Here
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
