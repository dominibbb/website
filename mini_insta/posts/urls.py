from django.urls import path
from . import views

app_name = 'posts'

urlpatterns= [
    path('create/', views.create_post, name='create_post'),
    # path('create', views.CreatePost.as_view(), name='create_post')

]
