from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import operator


# Create your views here.
def home(request):
    query = request.GET.get("title")
    allMovies = None
    if query:
        allMovies = Movie.objects.filter(intitulé__icontains=query)

    else:
        allMovies = Movie.objects.all()  # ==select * from movie

    ordered = sorted(allMovies, key=operator.attrgetter('nombreSorties'), reverse=True)

    context = {
            "movies": ordered
    }

    return render(request, 'main/index.html', context)


# detail page
def detail(request, id):
    movie = Movie.objects.get(id=id)  # select * from movie where id=id
    context = {
        "movie": movie
    }
    return render(request, 'main/details.html', context)


# add movies
def add_movies(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Si c'est ladmin qui est connecté
            if request.method == "POST":
                form = MovieForm(request.POST or None)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:home")
            else:
                form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movies"})
        else:  # if its not admin
            return redirect("main:home")
    else:  # If it is not logged in
        return redirect("accounts:login")

    # edit movie


def edit_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Si c'est ladmin qui est connecté
            movie = Movie.objects.get(id=id)
            if request.method == "POST":
                form = MovieForm(request.POST or None, instance=movie)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("main:detail", id)
            else:
                form = MovieForm(instance=movie)
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit Movies"})
        else:  # if its not admin
            return redirect("main:home")
    else:  # If it is not logged in
        return redirect("accounts:login")


# delete movie
def delete_movies(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:  # Si c'est ladmin qui est connecté
            movie = Movie.objects.get(id=id)
            movie.delete()
            return redirect("main:home")
        else:  # if its not admin
            return redirect("main:home")
    else:  # If it is not logged in
        return redirect("accounts:login")
