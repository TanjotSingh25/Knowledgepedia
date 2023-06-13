from django.shortcuts import render
from django import forms
from markdown import markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
import random as r

from . import util

class SearchForm(forms.Form):
    query = forms.CharField(label="")

class SearchForm_small(forms.Form):
    query = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Search'}))

class CreateMarkdown(forms.Form):
    title = forms.CharField(label="Title ", 
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'fill-area'}), required=True)
    content = forms.CharField(label="Content ", 
                              widget=forms.Textarea(attrs={'placeholder': 'Markdown Content', 'class': 'fill-area', 'rows': 25, 'cols': 40}), required=True)

class EditMarkdown(forms.Form):
    title = forms.CharField(label="Title ", 
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'fill-area', 'readonly': 'readonly'}),
                            required=True)
    content = forms.CharField(label="Content ", 
                              widget=forms.Textarea(attrs={'placeholder': 'Markdown Content', 'class': 'fill-area', 'rows': 25, 'cols': 40}),
                              required=True)

    # def __init__(self, title_value="", content_value="", *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs['value'] = title_value
    #     self.fields['content'].initial = content_value

def index(request):
    message = ''
    if 'message' in request.GET:
        message = request.GET.get('message')
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm(),
        'message': message
    })

def add_new_page(request):
    if request.method == "POST":
        form = CreateMarkdown(request.POST)
        message = "Error Creating Page"
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = f'# {title}\n\n' + form.cleaned_data["content"]
            if title in util.list_entries():
                message = "Page Already Exists"
            else:
                util.save_entry(title, content)
                message = "Page Successfully Added"
        return HttpResponseRedirect(reverse("index") + '?message=' + message)
    elif request.method == "GET":
        return render(request, "encyclopedia/create_page.html", {
            "form_search": SearchForm_small(),
            "form_createMarkdown": CreateMarkdown()
        })

def random(request):
    topic = r.choice(util.list_entries())
    return HttpResponseRedirect(reverse('render_page', kwargs={'topic': topic}))

def render_page(request, topic):
    if topic not in util.list_entries():
        message = "Page Doesnot Exists"
        return HttpResponseRedirect(reverse("index") + '?message=' + message)
    return render(request, "encyclopedia/topic.html", {
        "topic": topic,
        "form_search": SearchForm_small(),
        "content": util.get_entry(topic)
    })

def edit_page(request, topic):
    if request.method == "POST":
        form = EditMarkdown(request.POST)
        message = "Error Editing Page"
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if(title != topic):
                message = "This will not work here sucka"
            else:
                util.save_entry(title ,content.replace("\n", ""))
                message = "Page Successfully Edited"
        return HttpResponseRedirect(reverse("index") + '?message=' + message)
    elif request.method == "GET":
        return render(request, "encyclopedia/edit_page.html", {
            "topic": topic,
            "content": util.get_entry(topic),
            "form_search": SearchForm_small()
        })

def search_results(request):
    direct_hit = False
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = []
            for name in util.list_entries():
                if query.lower() == name.lower():
                    direct_hit = True
                    query = name
                if query.lower() in name.lower():
                    results.append(name)
    if direct_hit:
        return render(request, "encyclopedia/topic.html", {
        "topic": query,
        "form_search": SearchForm_small(),
        "content": util.get_entry(query)
    })
    else:
        return render(request, "encyclopedia/search_results.html", {
            "entries": results,
            "form": SearchForm()
        })