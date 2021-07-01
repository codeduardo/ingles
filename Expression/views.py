from django.shortcuts import render

from .models import Expression
# Create your views here.

def show_expr(request):
    expressions=Expression.objects.all()
    context={
        'expressions': expressions
    }
    return render(request,'Expression/list_expr.html',context)