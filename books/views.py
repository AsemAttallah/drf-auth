from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .permissions import OwnerOnly
# Create your views here.

class BookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[OwnerOnly]