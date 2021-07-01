from django.shortcuts import render

from .models import Word
# Create your views here.

def show_word(request):
    words = Word.objects.all()
    context= {
        'words': words
    }
    return render(request,'Word/list_word.html',context)
    