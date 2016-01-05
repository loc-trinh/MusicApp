from django.shortcuts import render
from youtube_api.models import Video


def youtube(request):
    context = {}
    if request.method == "POST":
        query = request.POST['query'].strip()
        videos = Video.remote.search(query)
        context["videos"] = videos[:10]
    return render(request, "YTD/youtube.html", context)


def frame(request):
    context = {}
    if request.method == "GET":
        context["url"] = request.GET["url"]
    return render(request, "YTD/frame.html", context)