from django.shortcuts import render,redirect,get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request,'blog/index.html', { 'memos': memos})

def detail(request, memo_id):
  memo = get_object_or_404(Memo, id=memo_id)
  return render(request, 'blog/detail.html', {'memo': memo})

@require_POST
def delete_memo(request,memo_id):
  memo = get_object_or_404(Memo, id=memo_id)
  memo.delete()
  return redirect('blog:index')

def edit_memo(request,memo_id):
  memo = get_object_or_404(Memo, id=memo_id)
  if request.method == "POST":
    form = MemoForm(request.POST, instance=memo)
    if form.is_valid():
      form.save()
      return redirect('blog:index')
  else:
    form = MemoForm(instance=memo)
  return render(request, 'blog/edit_memo.html', {'form':form, 'memo':memo})

def new_memo(request):
  if request.method == 'POST':
    form = MemoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('blog:index')

  else:
    form = MemoForm

  return render(request, 'blog/new_memo.html', {'form': form})