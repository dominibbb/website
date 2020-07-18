from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login1/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

]
