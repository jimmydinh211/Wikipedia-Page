from multiprocessing import context
from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from . import util
import random

# Create your views here.
def index(request, name):
    if (util.get_entry(name) == None):
        return render(request, "jimmipedia/error.html")
    else:
        return render(request, "jimmipedia/info_page.html", {"view_name": util.get_entry(name)})

#Homepage
def home (request):
    return render(request, "jimmipedia/index.html")

def random_method(request):
    ent = util.list_entries()
    name = random.choice(ent)
    return render(request, "jimmipedia/random_info_page.html", {"view_name": util.get_entry(name)})