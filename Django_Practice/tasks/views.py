from django.shortcuts import render
from django import forms

tasks = ['foo','bar','baz']

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")
    '''
    if you want to make a priority field-
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    '''

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        'tasks': tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request,POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form": form
                })

    return render(request, "tasks/add.html", {
        'form': NewTaskForm()
    })