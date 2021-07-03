from django.shortcuts import render,redirect

from .models import Expression
from .form import ExpressionForm 
# Create your views here.

def show_expr(request):
    expressions=Expression.objects.order_by('-id')
    form = ExpressionForm()
    
    if request.method=="POST":
        form = ExpressionForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('Expression')
    context={
        'expressions': expressions,
        'form':form
    }       
    return render(request,'Expression/list_expr.html',context)

def del_expr(request,id):
    expression = Expression.objects.get(id= id)  
    expression.delete()  
    return redirect('Expression')