from django.shortcuts import render
from datetime import date

all_posts=[
    {
        "slug": "the-mountains",
        "image": "mountains.jpg",
        "author": "Jason",
        "date": date(2024, 2, 28),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happend whilst I was enjoying the view!", 
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, dolore dolorem atque labore ea, 
                      at dicta ipsum mollitia tenetur quod voluptas a amet magni quia voluptate, explicabo cum incidunt. Rerum."""
    },
    {
    "slug": "Coding",
    "image": "coding.jpg",
    "author": "Jason",
    "date": date(2023, 4, 23),
    "title": "Coding is Great",
    "excerpt": "Coding is amazing, deep dive into pulling back the veil and exposing the matrix", 
    "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, dolore dolorem atque labore ea, 
                    at dicta ipsum mollitia tenetur quod voluptas a amet magni quia voluptate, explicabo cum incidunt. Rerum."""
    },
    {
    "slug": "woods",
    "image": "woods.jpg",
    "author": "Jason",
    "date": date(2021, 1, 22),
    "title": "Camping out in the Woods",
    "excerpt": "There's nothing like the views you get when hiking in the woods! And I wasn't even prepared for what happend whilst I was enjoying the view!", 
    "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, dolore dolorem atque labore ea, 
                    at dicta ipsum mollitia tenetur quod voluptas a amet magni quia voluptate, explicabo cum incidunt. Rerum."""
    },
]

def get_date(post):
    return post['date']

# Create your views here.
def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def single_post(request, post_title):
    identified_post = next(post for post in all_posts if post['slug'] == post_title)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })