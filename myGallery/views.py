from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Location
# Create your views here.
def gallery(request):
    all_pics=Image.objects.all()
    locations = Location.get_locations()
    return render(request, 'index.html',{"all_pics":all_pics[::-1], 'locations': locations})

 # GET image by location function    

def image_location(request,location):
    locations = Location.get_locations()
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'images': location,'locations': location})


# search function 
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
