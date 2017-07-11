# Arquivo: apps/users/urls.py
from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.RegistrationView.as_view(), name="register"),
    url(r'^playlist-tracks/(?P<playlist_id>\w{0,50})', views.playlisttracks, name="playlist-tracks"),
    url(r'^search/$', views.searchtrack, name="search"),
    url(r'^add-favorite-track/$', views.add_new_favorite_track, name='add_new_favorite_track'),
]
