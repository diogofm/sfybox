# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.template.defaulttags import register


from .forms import CustomUserCreationForm, TrackForm
from .models import MyUser, IdeaTrack
import apps.users.spotipy_functions as spotipy_manager


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_playlist_id(playlist):
    print(playlist['id'])
    return playlist['id']


@register.filter
def get_artist_name(track):
    return track['artists'][0]['name']


def add_new_favorite_track(request):
    context_dict = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TrackForm(request.POST)

            # Have we been provided with a valid form?
            if form.is_valid():
                # Save the new category to the database.
                    track = form.save(commit=False)
                    track.user = request.user
                    track.save()

                # Now call the index() view.
                # The user will be shown the homepage.
                    return home(request)
            else:
                # The supplied form contained errors - just print them to the terminal.
                print(form.errors)
        else:
            # If the request was not a POST, display the form to enter details.
            form = TrackForm()

        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
        return render(request, 'users/add-favorite-track.html', {'form': form})


def searchtrack(request):
    result_list = []
    context_dict = {}
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = spotipy_manager.search_tracks(query)
    context_dict['result_list'] = result_list
    context_dict['name'] = 'name'
    context_dict['id'] = 'id'

    return render(request, 'users/search.html', context_dict)


def playlisttracks(request, playlist_id):
    context_dict = {}
    context_dict['playlist_id'] = playlist_id
    if request.user.is_authenticated:
        playlist_tracks = spotipy_manager.show_playlist_tracks(request.user.spotify_username, playlist_id)
        print(playlist_tracks.__len__())
        context_dict['tracks'] = playlist_tracks
        context_dict['name'] = 'name'
        context_dict['id'] = 'id'
        context_dict['playlist_name'] = spotipy_manager.get_playlist_name(request.user.spotify_username, playlist_id)
    return render(request, 'users/playlist-tracks.html', context_dict)


def list_fav_tracks(query):
    list_fav = list()
    for e in query:
        list_fav.append(e)
    return list_fav


def home(request):
    context_dict = {}
    if request.user.is_authenticated:
        user_playlists = spotipy_manager.playlist_list(request.user.spotify_username)
        context_dict['playlists'] = user_playlists
        context_dict['name'] = 'name'
        try:
            context_dict['favorite_tracks'] = list_fav_tracks(IdeaTrack.objects.filter(user=request.user))
        except IdeaTrack.DoesNotExist:
            context_dict['favorite_tracks'] = None
    return render(request, 'users/home.html', context_dict)


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:login')
    return logout(request, *args, **kwargs)


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = "users/register.html"

