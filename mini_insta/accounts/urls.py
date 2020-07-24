from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from django.conf import settings


app_name = 'accounts'

urlpatterns = [
    path('login1/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name="profile"),
    path('update/<int:pk>/', views.ProfileUpdateView.as_view(), name='update'),
    path('email_change/<int:pk>/', views.email_change, name="email_change"),


    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html", 
        email_template_name='accounts/password_reset_email.html',
        success_url='/accounts/reset_password_sent/'),
        name='reset_password'),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_done.html",
        success_url='/accounts/reset_password_complete/'),
        name='password_reset_confirm'),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_succes"),
        name='password_reset_complete'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
