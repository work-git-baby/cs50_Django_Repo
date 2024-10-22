# CS50 Markdown Tutorial
>*Django is an extemely useful framework for making large-scale websites. It is quite comprehensive, so it's a good opportunity to me to practice markdown.*

## Getting started

### Initializing the first project

First things first, add django to your python library. 
```
pip install django
```


Then, you need to start a new project. In your terminal, run:
```
django-admin startproject <PROJECT_NAME>
```
This is to start the initial project.
>Note, there is a difference between a **Project** and an **App**
>A project is the overarching program and manages the overall layout.
>An app is the individual website cluster.
>You can initialize the project without any project by running the following command:```python manage.py runserver```
>This should show you the local ip and port you can use as a url.


Next, add the individual app.
```
python manage.py startapp <APP_NAME>
```


Now, you should see a new folder in the same directory tree as the project folder
This could get confusing quick, so I prefer to capitalize the project folder and name the app folders in lowercase.


### Creating our first app website

We can start by connecting the app to the project.
Here's how you do that:
1. **Make your App Known to the Project**
In your *project* folder, open settings.py.
 _ in the INSTALLED_APPS list, add the name of your app as a string.

2. **Link the App to the Project**
Still in your project folder, open urls.py
 _ We need to include one more import into the import section. Your import section should look like this:
 ```
 from django.contrib import admin
 from django.urls import include,path
 ```
 _ Then, in the list labeled urlpatterns, add the following code:
 ```
 path("APP_NAME>/", include("<APP_NAME>.urls"))
 ```
 This adds your future urls into the overall project. However, the app does not innately have urls. Thus,

3. **Make a Link for the App Webpage**
In the *app* folder, create a file called urls.py
 _ In your new urls.py file, we are mirroring the format of the urls.py in the project folder. Let's start with an index for the new app:
 ```
 from django.urls import path
 from . import views

 urlpatterns = [
    path("", views.index, name ="index")
 ]
 ```
 >This format of linking can be used to make more webpages as needed. 

4. **Make a function for the App Webpage**
Still in the app folder, open up views.py
 _ We need to render our new index link using a function. To start, we can add a function like this:
 ```
 def index(request):
    return render(request, "<app name>/index.html")
    ```
 _ This renders our index webpage if we type in our app name.

5. **Make an HTML File for the Webpage**
We need an actual html file to render.
 _ Create a folder called templates, then another folder named after the app.
 _ In the new directory, add a file called index.html
 -add the HTML for the index page.

Now, if you run ```python manage.py runserver```,you can visit the index you've created using the url for the server + the app name.

This process of making the website is pretty complex, but it is necessary to be familiar with all these different elements in Django in order to streamline manipulating multiple elements. In the next section, we will talk about the different functionalities provided by Django as presented by Harvard's CS50 course.

## Functionalites provided by Django




 

 






3)python manage.py runserver [runs test server, automatically refreshes with changes] 
[shows local ip and port]

4)python manage.py startapp <APP_NAME> [starts a new app]

add installed to settings.py -->INSTALLED_APPS+-

5)visit the new folder created for apps

6) views.py modifies what the user sees
    create func for new page

7)urls.py in the APP folder to call the function via urls

8)urls.py in the PROJECT folder to include urls in the overall project.

put {% load static %} to replace the css css link with a file somewhere in directory. Useful for big projects.

