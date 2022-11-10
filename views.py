from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import sys
import spotipy
import spotipy.util as util
# Create your views here.

def start_page(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        token = util.prompt_for_user_token(username, scope = "user-top-read",client_id= "1d0fac4c2a2740609f9574db39659e93",client_secret="74b6c1e8160742ae96623af71cd56047",redirect_uri="http://127.0.0.1:9090")

        if token:
            return HttpResponseRedirect(reverse('main_page', args=[username, token])) 

        else:
            return render(request, "login.html")

def main_page(request, username, token):
    return render(request, "main_page.html", {"username": username, "token" : token})

def top_tracks(request, username, token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit = 10, offset = 0, time_range = "short_term")

    tracks = results["items"]

    artists = []
    images = []
    track_names = []
    number_list = []

    number = 1

    for track in tracks:
        artists.append(track['artists'][0]['name'])
        images.append(track['album']['images'][0]['url'])
        track_names.append(track["name"])
        number_list.append(number)
        number = number + 1

    all_info = zip(artists, track_names, number_list, images)

    return render(request, "top_tracks.html", {"all_info":all_info, "username": username, "token" : token})

def top_genres(request, username, token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_artists(limit = 10, offset = 0, time_range = "short_term")["items"]

    top_genre_dict = {}

    for result in results:
        artist_genres = result["genres"]

        for artist_genre in artist_genres:
            if artist_genre not in top_genre_dict:
                top_genre_dict[artist_genre] = 1
            else :
                top_genre_dict[artist_genre] = top_genre_dict[artist_genre] + 1

    genre_value_list = sorted(top_genre_dict.items(), key=lambda x: x[1], reverse=True)

    top_genres = []
    top_values = []

    for genre_value in genre_value_list:
        if (len(top_genres) < 10):
            top_genres.append(genre_value[0])
            top_values.append(genre_value[1])

    
    return render(request, "top_genres.html", {"label": top_genres, "data": top_values, "username": username, "token" : token})

def new_releases(request, username, token):
    sp = spotipy.Spotify(auth=token)
    results = sp.new_releases()['albums']['items']

    artists = []
    images = []
    album_name = []
    number_list = []

    number = 1
    

    for result in results:
        album_name.append(result['name'])
        artists.append(result['artists'][0]['name'])
        images.append(result['images'][0]['url'])
        number_list.append(number)
        number = number + 1

    all_info = zip(artists, album_name, number_list, images)

    return render(request, "new_releases.html", {"all_info":all_info, "username": username, "token" : token})

def top_artists(request, username, token):
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_artists(limit = 10, offset = 0, time_range = "short_term")["items"]

        artists = []
        images = []
        number_list = []
        
        number = 1

        for result in results:
            artists.append(result["name"])
            images.append(result['images'][0]['url']) #done
            number_list.append(number)
            number = number + 1

            all_info = zip(artists, number_list, images)

        return render(request, "top_artists.html", {"all_info": all_info, "username": username, "token" : token})

