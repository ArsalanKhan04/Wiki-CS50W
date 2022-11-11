from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/pagenotfound.html")
    return render(request, "encyclopedia/page.html", {
        "title" : title,
        "content": util.get_entry(title)
    })

