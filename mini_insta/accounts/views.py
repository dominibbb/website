from django.shortcuts import render
#from django.urls import reverse_lazy
from django.views.generic.edit import FormView
#from django.views.generic import CreateView


from . import forms

# Create your views here.

# class SignUp(CreateView):
#     form_class = forms.UserCreationForm
#     success_url = reverse_lazy('home')
#     template_name = 'accounts/signup.html'



# OR THIS
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'user name or password is incorrect')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})
















#OR
# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = '/thanks/'

#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     form.send_email()
#     #     return super().form_valid(form)
