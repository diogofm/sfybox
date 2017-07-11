import spotipy, os
import spotipy.util as util

SPOTIPY_CLIENT_ID='3a6fe9230d9e42bd889589e50ef41d5d'
SPOTIPY_CLIENT_SECRET='06f5946c1cf04c67a0c71af93c2ca419'
SPOTIPY_REDIRECT_URI='http://localhost/'


scope = 'playlist-modify-public'
try:
    token = util.prompt_for_user_token('diogofm12', scope)
except:
    os.remove(".cache-"+'diogofm12')
    token = util.prompt_for_user_token('diogofm12', scope)