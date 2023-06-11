from django.shortcuts import render
from django import forms

from . import util

class SearchForm(forms.Form):
    query = forms.CharField(label="")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

