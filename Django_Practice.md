# CS50 Markdown Tutorial
>*Django is an extemely useful framework for making large-scale websites. It is quite comprehensive, so it's a good opportunity for me to practice markdown by taking notes.*

## Getting started  
### Initializing the first project  

First things first, add django to your python library.  
`pip install django`  

Then, you need to start a new project. In your terminal, run  
`django-admin startproject <PROJECT_NAME>`  
> Note, there is a difference between a **Project** and an **App**  
> A *project* is the overarching program and manages the overall layout.  
> An *app* is the individual website cluster.  
  
  
You can initialize the project without any project by running the following command:  
`python manage.py runserver`  
*This should show you the local ip and port you can use as a url.*
<br><br>
Next, add the individual app with
<br>
`
python manage.py startapp <APP_NAME>
`
<br>
*Now, you should see a new folder in the same directory tree as the project folder.*
<br>
> This could get confusing quick, so I prefer to capitalize the *project folder* and name the *app folders* in lowercase.

<br><br>

### Creating our first app website

> *For this example, we are going to make an index page.*    

We can start by connecting the app to the project. Here's how you do that:

#### **1. Make your App Known to the Project**
In your *project* folder, open `settings.py`. In the `INSTALLED_APPS` list, add the name of your app as a string. It should look like this:

 ```
 INSTALLED_APPS = [
    '<YOUR_APP_NAME>',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```


#### **2. Link the App to the Project**
Still in your project folder, open `urls.py`  

We need to include one more import, `include`, in order for the project to have access to all the different webpages in the app. Your import section should look like this:
 ```
 from django.contrib import admin
 from django.urls import include,path
 ```
 Then, in the list labeled `urlpatterns`, add the following code:

 ```
 path("<YOUR_APP_NAME>/", include("<APP_NAME>.urls"))
 ```

 *This adds your future urls into the overall project. However, the app does not innately have urls. Thus, we need to...*

#### **3. Make a Link for the App Webpage**
In the *app* folder, ***create a file*** called `urls.py`
 - In your new `urls.py` file, we are semi-mirroring the format of the urls.py in the *project* folder. Let's start with an index for the new app:
 ```
 from django.urls import path
 from . import views

 urlpatterns = [
    path("", views.index, name ="index")
 ]
 ```
 - This format of linking can be used to make more webpages as needed. 

#### **4. Make a function for the App Webpage**
Still in the app folder, open up `views.py`
 - We need to render our new index link using a function. To start, we can add a function like this:
 ```
 def index(request):
    return render(request, "<app name>/index.html")
```
 *This renders our index webpage if we type in our app name.*

#### **5. Make an HTML File for the Webpage**
We need an actual html file to render.
 1. Create a folder called templates, then another inside that folder named after the app.
 2. In the new directory, add a file called `index.html`
 3. Add the HTML for the index page.

Now, if you run ```python manage.py runserver```,you can visit the index you've created using the url for the server + the app name.
<br><br>

>*This process of making a website in Django is pretty complex, but it is necessary to be familiar with all these different elements in Django in order to manipulate multiple elements. In the next section, we will talk about the different functionalities provided by Django as presented by Harvard's CS50 course.*

## Functionalities Provided by Django
### Making Parameters for URLs
A lot of websites are dynamically created with the URL combinations provided. Here, we will give a cursory glance into how Django can help this process by creating a page that returns "Hello _____", depending on what name is passed through the URL address.

#### Making "Hello, _____"
First off, let's explore the `views.py` in the app folder.  
For simplicity's sake, we are just going to have Django return an HTTP response to give us an extremely simple website. to do this we need to import Django's http response function like this:  
```
from django.shortcuts import render
from django.http import HttpResponse
```
After that, we create a function that calls 2 parameters instead of 1. 
```
from django.shortcuts import render
from django.http import HttpResponse  
  
def index(request):
    return render(request, "<app name>/index.html")

def greet(request, name):
    return HttpResponse(f"Hello, {name}.")
```
In our new function, we are passing the argument `name` into what is returned, using it as a variable in our website that can be changed.  
  

Next, we need to add our greet function into our url patterns. In our `urls.py` file we need to make our new function known to the app.
```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ="index")
    path("<str:name>", views.greet, name="greet"),
]
```
>Note, that this is taking place within our *app* folder, not our *project* one.  
What `<str:name>` is telling Django is that we are passing a string into the path name and giving it to the function, greet, as a variable. Now, when we type in a name in <Port_Number>/<App_Name>/<Desired_Name>, Django returns the response "Hello, [whatever name you put in the url]".


 

 





<!--
3)python manage.py runserver [runs test server, automatically refreshes with changes] 
[shows local ip and port]

4)python manage.py startapp <APP_NAME> [starts a new app]

add installed to settings.py --INSTALLED_APPS+-

5)visit the new folder created for apps

6) views.py modifies what the user sees
    create func for new page

7)urls.py in the APP folder to call the function via urls

8)urls.py in the PROJECT folder to include urls in the overall project.

put {% load static %} to replace the css css link with a file somewhere in directory. Useful for big projects.

...

make forms in views.
-->
