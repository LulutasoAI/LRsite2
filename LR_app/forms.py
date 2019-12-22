from django import forms
from LR_app.models import Post, LRmachine

"""class HomeForm(forms.ModelForm):
    sid = forms.CharField()

    class Meta:
        model = Post
        fields = ("post", )

class auf(forms.Form):
    sid = forms.CharField()
"""


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title","text",)

class Syminput(forms.ModelForm):

    class Meta:
        model = LRmachine
        fields = ("stock_symbol",)
