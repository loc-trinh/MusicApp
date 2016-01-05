from django.shortcuts import render
from django.http import HttpResponse
from youtube_api.models import Video
from YTD.models import Playlist, Song
from download_song import download


def youtube(request):
    context = {}
    if request.method == "POST":
        query = request.POST['query'].strip()
        videos = Video.remote.search(query)
        context["videos"] = videos[:10]
        context["playlists"] = Playlist.objects.all()
    return render(request, "YTD/youtube.html", context)


def frame(request):
    context = {}
    if request.method == "GET":
        context["url"] = request.GET["url"]
    return render(request, "YTD/frame.html", context)


def add_to_download_queue(request):
    if request.method == "GET":
        url = request.GET["video_id"]
        video = Video.remote.fetch(url)[0]
        playlist = Playlist.objects.get(name=request.GET["playlist"])

        song = Song.objects.get_or_create(playlist=playlist, name=video.title)[0]
        song.url = url
        song.save()

    return HttpResponse("Added to queue.")


def downloads(request):
    context = {}
    songs = Song.objects.all()
    if len(songs):
        context["songs"] = songs
    return render(request, "YTD/downloads.html", context)


def download_video(request):
    if request.method == "GET":
        url = request.GET["url"]
        playlist = request.GET["playlist"]
        song_name = request.GET["song_name"]
        download(url, song_name, playlist)
        Song.objects.filter(name=song_name).delete()
    return HttpResponse("Finished downloading")