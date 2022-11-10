from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name=""),
    path("login/", views.login, name="login"),
    path("main_page/<str:username>/<str:token>'", views.main_page, name="main_page"),
    path("top_tracks/<str:username>/<str:token>'", views.top_tracks, name="top_tracks"),
    path("top_genres/<str:username>/<str:token>'", views.top_genres, name="top_genres"),
    path("new_releases/<str:username>/<str:token>'", views.new_releases, name="new_releases"),
    path("top_artists/<str:username>/<str:token>'", views.top_artists, name="top_artists"),
]