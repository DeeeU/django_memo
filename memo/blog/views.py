from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import TopForm
from .models import Top, Category

def index(request):
  photos = Top.objects.all().order_by('-created_at')
  return render(request, 'blog/index.html', {'photos': photos})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.top_set.all().order_by('-created_at')
    return render(request, 'blog/users_detail.html', {'user': user, 'photos': photos})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('blog:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required
def memo_new(request):
    if request.method == "POST":
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
        return redirect('blog:users_detail', pk=request.user.pk)
    else:
        form = TopForm()
    return render(request, 'blog/memo_new.html', {'form': form})


def memo_detail(request, pk):
    photo = get_object_or_404(Top, pk=pk)
    return render(request, 'blog/memo_detail.html', {'photo': photo})

@require_POST
def memo_delete(request, pk):
    photo = get_object_or_404(Top, pk=pk)
    photo.delete()
    return redirect('blog:users_detail', request.user.id)

def memo_category(request, category):
    category = Category.objects.get(title=category)
    photos = Top.objects.filter(category=category).order_by('-created_at')
    return render(request, 'blog/index.html', {'photos': photos, 'category':category})