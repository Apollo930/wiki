from django.shortcuts import render

from . import util
import markdown2, random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_entry(request):
    if request.method =="GET":
        return render(request, "encyclopedia/new_entry.html", {
            "entries": util.list_entries()
        })


def display_entry(request, title):
    content=util.get_entry(title)
    html= markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "entries": util.list_entries(),
        "title": title,
        "data": html
    })