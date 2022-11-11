from django.shortcuts import render
from django import forms
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

def search(request):
    if request == "GET":
        return render(request, "error.html")
    
    query = request.POST["q"]

    for entry in util.list_entries():
        if entry == query:
            return render(request, "encyclopedia/page.html", {
                "title" : entry,
                "content": util.get_entry(entry)
            })

    searchresult = []
    for entry in util.list_entries():
        if query in entry:
            searchresult.append(entry)
    return render(request, "encyclopedia/search.html", {
        "entries": searchresult
    })
    
