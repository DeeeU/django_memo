from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:memo_id>', views.detail, name='detail'),
    path('new_memo', views.new_memo, name='new_memo'),
    path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
    path('edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)