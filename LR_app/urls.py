#for my app
from django.urls import path
from LR_app import views
from django.conf.urls import url
import os


urlpatterns = [
    path("templates/", views.Lu_florchen, name="Top page"),
    path("test", views.test, name="test"),#idiotic saurce right below as well
    path("", views.index, name="index"),
    #url(r"testing/", views.auf , name="formtesting"),
    url("lranahome/", views.Anapage, name = "anapage1"),
    path(os.path.join("lranahome/", "analysisresult/"), views.analysis, name = "result"),
    #path("analysis", views.analysis_screen, name="analysis_screen"),
    path("symbolinput/", views.inputchan, name="inputchan"),
    #path("analysis/plot", views.img_plot, name="img_plot"),
    #path(r"output/", views.return_data),
    path("syminp/", views.syminpview, name = "syminpview"),
]
