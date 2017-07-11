import spotipy, webbrowser
from spotipy import oauth2
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import sys
import os
import subprocess
import spotipy.util as util
SPOTIPY_CLIENT_ID='3a6fe9230d9e42bd889589e50ef41d5d'
SPOTIPY_CLIENT_SECRET='06f5946c1cf04c67a0c71af93c2ca419'
SPOTIPY_REDIRECT_URI='http://localhost/'
token = "BQA6_xtKEhE84F7-jx_-1nNee_lCcTVRFKT7Uetpr6JjKNKxRHsWRC1lNNPLARgtBJLlWrdZEe0ithd8wOIzEfBZtqeGpiqDfBrU9xOECPRl_r0JUDzTEr_NVMrB3k3l7mmH7wrq2OizE7-E8MuPXhnax8Ag0PVGPK9at20eob7w75yfj8swass3QbWYiw"
def playlist_list(username):
    playlists_list = list()

    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlists = sp.user_playlists(username)
    while playlists:
        for playlist in enumerate(playlists['items']):
            playlists_list.append(playlist[1])
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    return playlists_list


def get_playlist_name(username, playlist_id):
    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp.user_playlist(username, playlist_id)['name']

def search_show_tracks(tracks):
    track_list = list()
    for i, item in enumerate(tracks['items']):
        track = item
        track_list.append(track)
    return track_list


def show_tracks(tracks):
    track_list = list()
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_list.append(track)
    return track_list


def show_playlist_tracks(username, playlist_id):
    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.user_playlist(username, playlist_id, fields="tracks,next")
    tracks = results['tracks']
    return show_tracks(tracks)


def search_tracks(query):
    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(query)
    tracks = results['tracks']
    return search_show_tracks(tracks)
