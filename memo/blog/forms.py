from django.forms import ModelForm
from .models import Top

class TopForm(ModelForm):
    class Meta:
        model = Top
        fields = ['title', 'short_comment', 'image', 'category']
