from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from django.template import loader

def index(request):
    #return HttpResponse("Hello, world. You're at CHOWMAN")
    #all_items = Items.objects.all()
    all_items = Items.objects.all().order_by('category')
    #breakpoint()
    template = loader.get_template("index.html")
    context = {
        "all_items": all_items,
    }
    #breakpoint()
    return HttpResponse(template.render(context, request))