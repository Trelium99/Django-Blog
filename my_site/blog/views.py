from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": Post.objects.all().order_by("-date")
    })

def single_post(request, post_title):
    identified_post = get_object_or_404(Post, slug=post_title)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })