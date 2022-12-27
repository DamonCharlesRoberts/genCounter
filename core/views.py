"""
    Title: views
    Notes:
        - Description: Takes the functions defined in models and forms. And defines functions used by urls.py to display the returned objects in the models.
        - Updated: 2022-12-23
        - Updated by: dcr
"""

from .models import Document
from .forms import DocumentForm

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

def DictPageView(request):
    Dict = Dictionary.objects.all()
    return render(request=request, template_name="show.html", context ={'word':Dict})

def ResultPageView(request):
    instance = Document.objects.latest("file")
    count = instance.WordCount()
    name = instance.FileName()
    return render(request=request, template_name="result.html", context={'name':name, 'count':count})

class CreateDocView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "form.html"
    success_url = reverse_lazy("home")
