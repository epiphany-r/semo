from django import forms
from . import models


class BookstoreCreateForm(forms.ModelForm):
    class Meta:
        model = models.Bookstore
        fields = [
            "bookstoreName",
            "bookstoreExp",
            "bookstoreAddress",
            "bookstoreTel",
            "bookstorePic",
        ]
        widgets = {
            "bookstoreName": forms.TextInput(
                attrs={
                    "class": "container flex mb-4 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "bookstoreExp": forms.Textarea(
                attrs={
                    "class": "container flex appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "bookstoreAddress": forms.TextInput(
                attrs={
                    "class": "container flex appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "bookstoreTel": forms.TextInput(
                attrs={
                    "class": "container flex appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
        }
