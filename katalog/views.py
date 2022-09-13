from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

def show_catalog(request):
    catalog = CatalogItem.objects.all()
    return render(
        request,
        "katalog.html",
        {
            "name": "Ruben Tanoey",
            "student_id": "2106752445",
            "catalogs": catalog,
        },
    )