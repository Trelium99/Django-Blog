from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("posts", views.posts, name="posts-page"),
    path("post/<slug:post_title>", views.single_post, name="post-details-page"),
]
