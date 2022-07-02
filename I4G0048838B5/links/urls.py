from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostListAPI, PostCreateAPI, PostDetailAPI, PostUpdateAPI, PostDeleteAPI
from . import views 

router = DefaultRouter()
router.register(r'link', PostListAPI, PostCreateAPI,PostDetailAPI, PostUpdateAPI, PostDeleteAPI)

app_name="link"

urlpatterns = [
    path("create/", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view(), name="api_delete"),
    path("", views.PostListApi.as_view(), name="api_list"),
] + router.urls