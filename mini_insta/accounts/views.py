from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import HttpResponse

from . import forms

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import SignupForm



from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import  login_required

from django.core.mail import EmailMessage
from .tokens import account_activation_token, email_activation_token
from django.core.mail import send_mail

from django.contrib.auth.models import User
from .models import EmailChangeAuth

from django.contrib import messages

@login_required
def emial_change(request):
    User = get_user_model()
    if 'change_email' in request.POST:
        new_email = request.POST.get('new_email')
        user = request.user
        EmailChangeAuth.objects.create(user=user, new_email=new_email)

        mail_subject = 'Confirm new email'
        current_site = get_current_site(request)
        message = render_to_string('accounts/email_template_change_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': email_activation_token.make_token(user)
        })
        send_mail(mail_subject, message, 'dev.django.git@gmail.com', [new_email])
        return HttpResponse('Check your email and confirm your new email address')
    
    context = {

    }

    return render(request, 'accounts/change_email.html', context)


def new_email_activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and email_activation_token.check_token(user, token):
        email_change = EmailChangeAuth.objects.get(user=user)
        email_change.save_changes()
        email_change.delete()
        return HttpResponse('Thank you for your email confirmation. Your email is change')
    else:
        return HttpResponse('Activation link is invalid!')
    

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'dev.djang.git@gmail.com', [to_email])
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()

    return render(request, 'accounts/regform.html', {'form': form})


        

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



from .forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'user name or password is incorrect')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})



from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Profile
from django.urls import reverse_lazy

class ProfileView(DetailView):

    model = Profile
    template_name = 'accounts/profile_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProfileUpdateView(UpdateView):

    model = User
    template_name = 'accounts/update_profile.html'

    fields = ['username', 'email']

    success_message = "Updated Successfully" 
    success_url = reverse_lazy('accounts:profile')