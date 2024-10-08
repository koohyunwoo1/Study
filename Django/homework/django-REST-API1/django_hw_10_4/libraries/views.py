from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    try:
        book = Book.objects.get(pk=book_pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        book_title = book.title
        book_isbn = book.isbn
        book.delete()
        message = {'delete': f'도서 고유번호 {book_isbn}번의 {book_title}을 삭제하였습니다.'}
        return Response(message, status=status.HTTP_200_OK)
