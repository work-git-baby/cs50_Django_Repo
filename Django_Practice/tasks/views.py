from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

'''
This was the original way to create the task list(before talking about sessions)
tasks = ['foo','bar','baz']
'''

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    '''
    if you want to make a priority field-
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    '''

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        'tasks': request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
    })