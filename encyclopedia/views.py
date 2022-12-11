from django.shortcuts import render

from . import util
import markdown2, re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_entry(request, title=""):
    if request.method =="GET":
        if title:       #editing an existing entry
            content=util.get_entry(title)
        else:           #creating a new entry
            content=""

        return render(request, "encyclopedia/new_entry.html", {
            "entries": util.list_entries(),
            "title": title,
            "content": content,
        })

    elif request.method =="POST":    #creating a new entry
        if request.POST.get("title", False):
            title, content= request.POST["title"], request.POST["content"]
            if title not in util.list_entries():
                util.save_entry(title, content)
                return display_entry(request, title)
            else:
                return render(request, 'error_page.html', {
                    'entries': util.list_entries(),
                    'error_message':"There is already an entry with the same name."
                } )

        else:       #editing an existing entry
            title, content = request.POST.get("old_title"), request.POST.get("content")
            util.save_entry(title, content)
            return display_entry(request, title)

def edit_entry(request, title):
    content=util.get_entry(title)
    return render(request, "encyclopedia/new_entry.html", {
        "entries": util.list_entries(),
        "content": content
    } )

def display_entry(request, title):
    content=util.get_entry(title)
    html= markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "entries": util.list_entries(),
        "title": title,
        "data": html
    })

def search_entry(request):
    title=request.POST.get("q")
    if title in util.list_entries():
        return display_entry(request, title)
    else:
        search_results=[]
        for entry in util.list_entries():
            if re.search(title, entry, re.IGNORECASE):
                search_results.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": search_results,
        })