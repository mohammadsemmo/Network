
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("following", views.following, name="following"),

    # API Routes
    path("entity/like/<int:entity_id>", views.like, name="like"),
    path("entity/unlike/<int:entity_id>", views.unlike, name="unlike"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("unfollow/<int:user_id>", views.unfollow, name="unfollow"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("upload_image", views.upload_image, name="upload_image")

]