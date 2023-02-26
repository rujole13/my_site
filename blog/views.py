from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def starting_page(request):
     return render(request, "blog/index.html")
     # return HttpResponse("Test")

def posts(request):
    try:
        return render(request, "blog/all-posts.html")
    except:
        raise Http404()
    

def post_detail(request, slug):
    if slug == "the-mountains":
        try:
            return HttpResponse("post detail is working!")
        except:
            raise Http404()
