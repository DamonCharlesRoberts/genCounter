"""
    Title: views
    Notes:
        - Description: Takes the functions defined in models and forms. And defines functions used by urls.py to display the returned objects in the models.
        - Updated: 2022-12-23
        - Updated by: dcr
"""

from django.shortcuts import render #to render the models and forms
from django.views.generic import CreateView #to render dictionary
from django.urls import reverse_lazy #once file is uploaded, send it to a new url while analysis is executed
from django_pandas.io import read_frame #read_frame for the loaded dictionary table
from .models import Document, Dictionary #to access the Document and Dictionary models
from .forms import DocumentForm #to access the DocumentForm

def HomePageView(request):
    """
        Name: HomePageView
        Description: Renders the home page
        Dependencies:
            - django.shortcuts.render
            - templates/home.html
    """
    return render(request=request, template_name='home.html') # render the contents of templates/home.html

def AboutPageView(request):
    """
        Name: AboutPageView
        Description: Renders the about/documentation page
        Dependencies:
            - django.shortcuts.render
            - templates/about.html
    """
    return render(request=request, template_name='about.html') # render the contents of templates/about.html

def DictPageView(request):
    """
        Name: DictPageView
        Description: Renders the page displaying a table of the dictionary
        Dependencies:
            - django.shortcuts.render
            - core.models.Dictionary
            - templates/show.html
    """
    Dict = Dictionary.objects.all() # take the Dictionary model (which is the dictionary table)
    return render(request=request, template_name="show.html", context ={'word':Dict}) # and render the table and call the Dict object "word" for access in the template

def ResultPageView(request):
    """
        Name: ResultPageView
        Description: Once CreateDocView is executed, it then performs the analysis on the document and presents the results
        Dependencies:
            - django.shortcuts.render
            - core.models.Document
            - core.models.Dictionary
            - django_pandas.io.read_frame
            - template/result.hml
    """
    instance = Document.objects.latest("file") # take the latest file uploaded with the Document model
    dict = read_frame(Dictionary.objects.all()) # grab the contents of the dictionary table passed by the Dictionary model and read it as a pandas DataFrame
    count = instance.WordCount() # take the WordCount of the document
    name = instance.FileName() # take the FileName of the document
    score = instance.Score(dict) # pass the dictionary to the Score function and calculate the score for the file
    return render(request=request, template_name="result.html", context={'name':name, 'count':count, 'score':score}) # render the result of the WordCount, FileName, and Score and store them as name, count, and score for template 

class CreateDocView(CreateView):
    """
        Name: CreateDocView
        Description: Create a form for people to upload the file to
        Dependencies:
            - django.view.generic.CreateView
            - core.models.Document
            - core.forms.DocumentForm
            - templates/form.html0
    """
    model = Document # take the Document Object
    form_class = DocumentForm # and put it in a form
    template_name = "form.html" # put the form in templates/form.html
    success_url = reverse_lazy("result") # and if the file is successfully uploaded, send it to the result page
