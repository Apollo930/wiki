from django.shortcuts import render

from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_entry(request, title=""):
    if request.method =="GET":
        if title:
            content=util.get_entry(title)
        else:
            content=""
        return render(request, "encyclopedia/new_entry.html", {
            "entries": util.list_entries(),
            "content": content,
        })

    else:
        title, content= request.POST["title"], request.POST["content"]
        if title not in util.list_entries():
            util.save_entry(title, content)
            return display_entry(request, title)
        else:
            return render(request, 'error_page.html', {
                'error_message':"There is already an entry with the same name."
            } )

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