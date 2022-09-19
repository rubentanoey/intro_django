from django.shortcuts import render

# TODO: Create your views here.
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_xml_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    return render(request, 'mywatchlist.html')

def show_watchlist(request):
    watchlists = MyWatchList.objects.all()
    return render(
        request,
        "mywatchlist.html",
        {
            "name": "Ruben Tanoey",
            "student_id": "2106752445",
            "watchlists": watchlists,
        },
    )