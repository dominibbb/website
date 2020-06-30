from django.urls import path
from . import views

app_name = 'posts'

urlpatterns= [
    path('create/', views.create_post, name='create_post'),
    # path('list/', views.list_view, name='list'),
    path('list/', views.PostListView.as_view(), name='list'),
    # path('detail/<int:pk>', views.detail_view, name='detail'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('comment/', views.add_comment, name='comment'),

]
