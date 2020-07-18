from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# ACCOUNTS FORMS.PY

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
   
#     class Meta:
#         model = get_user_model()
#         fields = ("username", "email", "password1", "password2")
 
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

