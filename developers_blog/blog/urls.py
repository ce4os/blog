from django.urls import path
from .views import about_view, home_view, detail_view

urlpatterns = [
    path("", home_view, name="home"),
    path("detail/<int:post_id>", detail_view, name="detail"),
    path("about/", about_view, name="about")
]