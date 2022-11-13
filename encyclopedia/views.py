from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse


class contentForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")


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
            return HttpResponseRedirect(reverse("page", kwargs={"title":entry}))

    searchresult = []
    for entry in util.list_entries():
        if query in entry:
            searchresult.append(entry)
    return render(request, "encyclopedia/search.html", {
        "entries": searchresult
    })
    


def newpage(request):
    existing = False
    if request.method == "POST":
        print("request for post is working")
        form = contentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                existing = True
            else:
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("page", kwargs={"title":title}))
    else:
        form = contentForm()


    return render(request, "encyclopedia/newpage.html", {"form":form, "existing":existing})
    
def editpage(request):
    return None