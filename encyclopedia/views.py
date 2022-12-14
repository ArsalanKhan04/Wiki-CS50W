from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
import random as rn
from . import convertMark

class contentForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea)

class editForm(forms.Form):
    content = forms.CharField(label="Content", widget = forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })




def wiki(request, title):
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/pagenotfound.html")
    return render(request, "encyclopedia/wiki.html", {
        "title" : title,
        "content": convertMark.convert(util.get_entry(title))
    })




def search(request):
    if request == "GET":
        return render(request, "error.html")
    
    query = request.POST["q"]

    for entry in util.list_entries():
        if entry == query:
            return HttpResponseRedirect(reverse("wiki", kwargs={"title":entry}))

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
                return HttpResponseRedirect(reverse("wiki", kwargs={"title":title}))
    else:
        form = contentForm()


    return render(request, "encyclopedia/newpage.html", {"form":form, "existing":existing})
    
def editpage(request, title):
    print(title)
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/pagenotfound.html")
    
    if request.method == "POST":
        form = editForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("wiki", kwargs={"title":title}))
    else:
        form = editForm(initial = {
            "content": convertMark.convert(util.get_entry(title))
        })

    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "form": form
    })

def random(request):
    randomtitle = rn.choice(util.list_entries())
    return HttpResponseRedirect(reverse("wiki", kwargs={
        "title":randomtitle
    }))
