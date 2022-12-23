"""
    Title: urls
    Notes:
        - Description: Takes the defined views functions and assigns them a url to display
        - Updated: 2022-12-23
        - Updated by: dcr

"""

from django.urls import path # for url path management
from .views import HomePageView, AboutPageView, ResultPageView, CreateDocView, DictPageView # pull in the defined views that I want to display on webpage

urlpatterns = [ # define the url patterns for the pages in the core app I want to display
    path("", HomePageView, name = "home"), # put the HomePageView on the landing page
    path("about/", AboutPageView, name = "about"), # put the AboutPageView on about/
    path("upload/", CreateDocView.as_view(), name="upload_file"), # put the CreateDocView on upload/
    path("dictionary-preview/", DictPageView, name = 'dictionary'), # put the DictPageView on dictionary-preview/
    path("result/", ResultPageView, name="result") # put the ResultPageView on result/
]