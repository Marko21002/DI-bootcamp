from django.shortcuts import render
from .forms import CategoryForm, GifForm
from .models import Category, Gif
from django.http import HttpResponse

# Add new GIF view


def add_gif_view(request):

    # GET mode - getting content out

    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        # put the data from the request into the ModelForm
        gif_filled_form = GifForm(request.POST)

        if gif_filled_form.is_valid():  # check if all fields contain the correct data
            gif_filled_form.save()  # save data into database
            return HttpResponse("SUCCESSFULLY SAVED")

    if request.method == 'GET':
        gif_form = GifForm()
        print("GET data: ", request.GET)  # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': gif_form}

    return render(request, 'add_gif.html', context)


# Add new Category view
def add_category_view(request):
    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        # put the data from the request into the ModelForm
        category_filled_form = CategoryForm(request.POST)

        if category_filled_form.is_valid():  # check if all fields contain the correct data
            category_filled_form.save()  # save data into database
            return HttpResponse("SUCCESSFULLY SAVED")

    if request.method == 'GET':
        category_form = CategoryForm()
        print("GET data: ", request.GET)  # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': category_form}

        return render(request, 'add_gif.html', context)


def gifs_viev(request):

    gifs_all = Gif
