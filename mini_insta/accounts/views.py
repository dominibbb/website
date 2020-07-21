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

from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.core.mail import send_mail

from django.contrib.auth.models import User

from django.contrib import messages

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        print('method post')
        form = SignupForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            print('form is valid')
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
            send_mail(mail_subject, message, 'lewy12345678910@gmail.com', [to_email])
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

from django.contrib.auth import authenticate, login

# def my_view(request):
#     if requ
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('home')

#     else:
#         messages.error(request, 'user name or password is incorect')

#     return render(request, 'accountd/login.html', {})