from django.shortcuts import render

from .models import Verb
# Create your views here.

def show_verb(request):
    verbs=Verb.objects.all()
    context={
        'verbs':verbs
    }
    return render(request,'Verb/listVerb.html',context)
    