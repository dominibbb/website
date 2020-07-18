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
from .tokens import activation_token

from django.contrib.auth.models import User

from django.contrib import messages

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_date.get('email')
            if form.cleaned_date.get(email__iexact=email).count() == 1:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('email_tmplate.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                send_mail(mail_subject, message, 'lewy12345678910@gmail.com', [to_email])
                return HttpResponse('Please confirm your email addres')

    else:
        form = forms.SignupForm()
    return render(request, 'accounts/regform.html', {'form': form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your email is confirm. Now you can log in')
    else:
        return HttpResponse('This link is invalid!')

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


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

# for changing password
# update_session_auth_hash(request, form.user)