from django.urls import path

<<<<<<< HEAD
from .views import HomePageView, AboutPageView, CreateDocView, DictPageView
=======
from .views import HomePageView, AboutPageView, ResultPageView, CreateDocView, DictPageView
>>>>>>> e3ac996 (word count analyzer)

#urlpatterns = [
#    path('', views.home, name='home'),
#    path('', views.model_form_upload, name='upload')
#]

urlpatterns = [
    path("", HomePageView, name = "home"),
    path("about/", AboutPageView, name = "about"),
    path("upload/", CreateDocView.as_view(), name="upload_file"),
<<<<<<< HEAD
    path("dictionary-preview/", DictPageView, name = 'dictionary')
=======
    path("dictionary-preview/", DictPageView, name = 'dictionary'),
    path("result/", ResultPageView, name="result")
>>>>>>> e3ac996 (word count analyzer)
]