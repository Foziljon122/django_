from django import forms
from.models import User

from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     foydalanuvchi_nomi = models.CharField(max_length=255)
#     parol = models.CharField(max_length=255)
#     elektron_pochta = models.EmailField()
#     date_joined = models.DateTimeField(auto_now_add=True)

# from django import forms
# from .models import UserProfile

# class RoxyatdanOtishForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['foydalanuvchi_nomi', 'parol', 'elektron_pochta']

# class LoginForm(forms.Form):
#     foydalanuvchi_nomi = forms.CharField(max_length=255)
#     parol = forms.CharField(max_length=255, widget=forms.PasswordInput())
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import RoxyatdanOtishForm, LoginForm

# def roxyatdan_otish(request):
#     if request.method == 'POST':
#         form = RoxyatdanOtishForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['parol'])
#             user.save()
#             return redirect('login')
#     else:
#         form = RoxyatdanOtishForm()
#     return render(request, 'roxyatdan_otish.html', {'form': form})

# def tizimga_kirish(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             foydalanuvchi_nomi = form.cleaned_data['foydalanuvchi_nomi']
#             parol = form.cleaned_data['parol']
#             user = authenticate(request, username=foydalanuvchi_nomi, password=parol)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')  # 'index' sizning bosh sahifangizni ko'rsatkich
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
# from django.urls import path
# from .views import roxyatdan_otish, tizimga_kirish

# urlpatterns = [
#     path('roxyatdan_otish/', roxyatdan_otish, name='roxyatdan_otish'),
#     path('login/', tizimga_kirish, name='login'),
    # Boshqa URL patternlarni ham qo'shishingiz mumkin
# ]



            # class MessageForm(forms.Form):
            #     name = forms.CharField(max_length=100)
            #     message = forms.CharField(widget=forms.Textarea)


            # from django.urls import path
            # from .views import message_create

            # urlpatterns = [
            #     path('message_create/', message_create, name='message_create'),
            # ]


            # from django.contrib import admin
            # from django.urls import include, path

            # urlpatterns = [
            #     path('admin/', admin.site.urls),
            #     path('', include('myapp.urls')),
            # ]


            # from django import forms

            # class MessageForm(forms.Form):
            #     name = forms.CharField(max_length=100)
            #     message = forms.CharField(widget=forms.Textarea)

            #     def clean(self):
            #         cleaned_data = super().clean()
            #         name = cleaned_data.get('name')
            #         message = cleaned_data.get('message')

            #         if not name:
            #             raise forms.ValidationError('Ism maydoni to\'ldirilishi shart')
                    
            #         if not message:
            #             raise forms.ValidationError('Xabar maydoni to\'ldirilishi shart')


