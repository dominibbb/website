from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('create/', views.create_group, name='group'),
    path('list/', views.GroupListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.GroupDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.GroupDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.GroupUpdateView.as_view(), name='update')
]