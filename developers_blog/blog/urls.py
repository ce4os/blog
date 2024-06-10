from django.urls import path
from .views import about_view, detail_view, home_view, imprint_view, privacy_policy_view
urlpatterns = [
    path("", home_view, name="home"),
    path("detail/<int:post_id>", detail_view, name="detail"),
    path("about/", about_view, name="about"),
    path("imprint/", imprint_view, name="imprint"),
    path("privacy_policy/", privacy_policy_view, name="privacy_policy"),
]