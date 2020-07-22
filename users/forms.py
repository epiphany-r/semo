from .models import User, likebook
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django import forms

book_choices = [
    ("Photo", "사진"),
    ("construct", "건축, 지역"),
    ("record", "음반"),
    ("design", "디자인"),
    ("movie", "영화"),
    ("literature", "문학, 비평"),
    ("Experiment", "주제, 실험"),
    ("magazine", "잡지"),
    ("illustration","일러스트레이션, 회화, 만화"),
    ("Illustrated book","도감"),
    
]


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        label="회원ID",
        strip=False,
        widget=forms.TextInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )

    likebooks = forms.MultipleChoiceField(
        label="관심장르",
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "font-medium tracking-wider text-gray-700"}
        ),
        choices=book_choices,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "nickName",
            "userEmail",
            "userAddress",
            "userTel",
            "writerIntro",
            "likebooks",
            "userPic",
        ]

        widgets = {
            "nickName": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userEmail": forms.EmailInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userAddress": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "userTel": forms.TextInput(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
            "writerIntro": forms.Textarea(
                attrs={
                    "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
                }
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # print(self.cleaned_data['likebooks'])
        if commit:
            user.save()
            for book in self.cleaned_data["likebooks"]:
                lb = likebook(userID=user, bookCategoryID=book)
                lb.save()

        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="회원ID",
        widget=forms.TextInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )
    password = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "container flex bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-green-500"
            }
        ),
    )


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['nickName', 'userEmail', 'userAddress', 'userTel', 'writerIntro']
