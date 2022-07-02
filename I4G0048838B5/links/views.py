from django.shortcuts import render
import rest_framework.generics
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Link
from rest_framework import serializers
from .serializers import LinkSerializer

# Create your views here.
class PostListAPI(ListAPIView.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateAPI(CreateAPIView.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailAPI(RetrieveAPIView.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateAPI(UpdateAPIView.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteAPI(DestroyAPIView.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer