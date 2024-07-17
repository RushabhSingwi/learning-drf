from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("", views.blog_view, name="home"),
    path("blogs/", views.blogs, name="blog"),
    path("signup/", views.sign_up, name="signup"),
    re_path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]