from django import forms
from .models import WriterBlog


class writersblogCreateForm(forms.ModelForm):
    class Meta:
        model = WriterBlog
        fields = ["postTitle", "postExp", "postPic"]
        widgets = {
            "postTitle": forms.TextInput(attrs={"class": "form-control"}),
            "postExp": forms.Textarea(attrs={"class": "form-control"}),
        }
