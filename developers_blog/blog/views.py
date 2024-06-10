from django.shortcuts import render
from .models import BlogPost

def get_latest_posts():
    return BlogPost.objects.all()[:3]

# Create your views here.
def home_view(request):
    queryset = get_latest_posts()
    context = {"queryset":queryset}
    return render(request, "blog/home.html", context)


def detail_view(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    context = {"post":post}
    return render(request, "blog/detail.html", context)

def about_view(request):
    return render(request, "about.html")

def imprint_view(request):
    return render(request, "imprint.html")

def privacy_policy_view(request):
    return render(request, "privacy_policy.html")