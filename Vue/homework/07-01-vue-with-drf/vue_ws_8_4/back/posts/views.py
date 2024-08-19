from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import PostListSerializer, CategorySerializer, PostSerializer, CommentSerialzer
from .models import Post, Category, Comment

# Create your views here.

@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialzers = PostListSerializer(posts, many=True)
        return Response(serialzers.data)
    elif request.method == 'POST':
        category = Category.objects.get(pk=request.data.get('category'))
        serialzer = PostSerializer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save(category=category)
            return Response(serialzer.data)
        
@api_view(['GET'])
def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    serialzer = PostSerializer(post)
    return Response(serialzer.data)

@api_view(['POST'])
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    serialzer = CommentSerialzer(data=request.data)
    if serialzer.is_valid(raise_exception=True):
        serialzer.save(post=post)
        return Response(serialzer.data)