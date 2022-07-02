from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Link
from rest_framework import serializers
from .serializers import LinkSerializer


# Create your views here.
class PostListAPI(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateAPI(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailAPI(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateAPI(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteAPI(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer