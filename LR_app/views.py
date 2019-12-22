from django.shortcuts import render
from django.http import HttpResponse
import io
import matplotlib.pyplot as plt
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import TemplateView
#from LR_app.forms import HomeForm
#from LR_app.forms import auf
from LR_app.models import LRmachine
#from LR_app.forms import Symboldecider
import os
from .forms import PostForm, Syminput
from django.utils import timezone

inpc ="GOOG"
#testing for learning fucking forms
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def etwas(request):
    f = auf()
    return HttpResponse(f)
#from boards.forms import SidForm
#from library.models import LinearRG
# Create your views here.

def inputchan(request):
    if request.method == "POST":
        form = PostForm()
        return render(request, "post_edit.html", {'form': form})
    else:
        return render(request, "post_edit.html")

def syminpview(request):
    syminpform = Syminput(request.POST)
    if request.method == "POST":
        if syminpform.is_valid():
            sid = str(syminpform.save())
            LRmachine.Converter(sid)
            return render(request, "result.html")
            #HttpResponse("1,{} and 2,{}".format(sid, LRmachine.inpc))
            #"""LRmachine.Converter(sid)""" wait a minute

        else:
            return render(request, "analy.html", {"syminpform":syminpform})
    else:
        return render(request, "analy.html", {"syminpform":syminpform})

def sidcreater(request):
    if request.method == "POST": # if the form has been submitted...
        form = Stockinput(request.POST) #A form bound to the POST data
        if form.is_valid():#ALL valuidation rules pass
            #process the data in from.cleaned_data
            sid = form.cleaned_data("sid")
            LRmachine.Converter(sid)
            return HttpResponseRedirect("/analysisresult/")
        else:
            form = Stockinput() #unbound

def Inputchan(request):
    auf = (PostForm)
    return render(request, "analy.html", {"form": form})


def image_test(request):
    image_file = open(os.path.join(BASE_DIR, "files", "picture.png"), "rb").read()


def home(request):
    return HttpResponse("Hallo, Welt!")
def Lu_florchen(request):
    return render(request, "index.html")

#very importtant below
def Anapage(request):
    return render(request, "analy.html")

def analysis(request):
    return render(request, "result.html")

class HomeView(TemplateView):
    template_name = "analy.html"

    def stockchs(self, request):
        sid = HomeForm(request.POST)
        LRmachine.Converter(sid)


        return render(request, self.templete_name)

def test(request):
    return render(request, "index.html")

def index(request):
    return render(request, "index.html")

class HomeView(TemplateView):
    template_name = "analy.html"

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {"form":form})
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            post.user= request.user
            post.save()
            text = form.cleaned_data["post"]
            form = HomeForm()
        args = {"form": form, "text": text}
        return render(request, self.templete_name, args)


#plt to png
"""def plt2png():
    buf = io.BytesIO()
    plt.savesig(buf, format="png", dpi=200)
    s = buf.getvalue()
    buf.close()
    return s"""

#describe html view
"""def analysis_screen(request):
    return render(request, "analysis.html")"""

#generate the chart
"""def img_plot(request):
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type="image/png")
    return response
"""
#implement picture view
"""def img_plot(request):
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type="image/png")
    return response
"""
    #matplot wo tukatte sakuszu

"""def get_id(request):
    if request.method =="POST":
        form = SidForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/confirmed the id/")
    else:
        form = SidForm()

    return render(request, "analysys.html")
"""
"""def return_data(request):
    return HttpResponse(models.LinearRG.Linear_Regression_converter(request.POST["text"]))
"""
# Create your views here.
