from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import CreateUserForm, UserLoginForm
from .models import User
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

class CreateUserView(CreateView):
    model = User
    template_name = 'users/Join_Form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'users/Login_Form.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

@login_required
def update(request):
    if request.method == 'Post':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:people', request.user.username)
        else:
            user_change_form = CustomUserChangeForm(instance=request.user)
            return render(request, 'users/update.html',{'user_change_form':user_change_form})