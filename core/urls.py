from django.urls import path

from .views import HomePageView, AboutPageView, CreateDocView

#urlpatterns = [
#    path('', views.home, name='home'),
#    path('', views.model_form_upload, name='upload')
#]

urlpatterns = [
    path("", HomePageView, name = "home"),
    path("about/", AboutPageView, name = "about"),
    path("upload/", CreateDocView.as_view(), name="upload_file")
]