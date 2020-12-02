from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse
from .models import *
from .forms import *
from django.conf import settings

from django.contrib.auth.decorators import login_required
# Create your views here.

from .tasks import long_taks

def newtask(request, id):
    token = long_taks.delay(id)
    return HttpResponse(f"NEW TASK: {token}")

def error(request):
    raise TypeError("Invalid type")
    return HttpResponse("OK")

def startpage_response(request):
    return HttpResponse(request.user.username)

def movielist_response(request):
    all_movies = Movie.objects.all().order_by("title")
    return render(request, "movie-list.html",
                  { "movies":all_movies,
                    "media_url": settings.MEDIA_URL } )


@login_required()
def movieadd_response(request):

    #if not request.user.is_authenticated:
    #    return redirect(settings.LOGIN_URL)

    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.created_by = request.user
        movie.save()
        return redirect(movielist_response)
    return render(request, "movie-add.html", {"form" : form})

def logout_done(request):
    return render(request, "logout-done.html")