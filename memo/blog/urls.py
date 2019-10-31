from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    path('top/<int:pk>/', views.memo_detail, name='memo_detail'),
    path('top/new/', views.memo_new, name='memo_new'),
    path('top/<int:pk>/delete/', views.memo_delete, name='memo_delete'),
    path('top/<str:category>/', views.memo_category, name='memo_category'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]