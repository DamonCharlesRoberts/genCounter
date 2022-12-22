from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django_pandas.io import read_frame
from .models import Document, Dictionary
from .forms import DocumentForm

def HomePageView(request):
    return render(request=request, template_name='home.html')

def AboutPageView(request):
    return render(request=request, template_name='about.html')

def DictPageView(request):
    Dict = Dictionary.objects.all()
    return render(request=request, template_name="show.html", context ={'word':Dict})

def ResultPageView(request):
    instance = Document.objects.latest("file")
    dict = read_frame(Dictionary.objects.all())
    count = instance.WordCount()
    name = instance.FileName()
    score = instance.Score(dict)
    return render(request=request, template_name="result.html", context={'name':name, 'count':count, 'score':score})

class CreateDocView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "form.html"
    success_url = reverse_lazy("result")
