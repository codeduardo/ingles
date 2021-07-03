from django.forms import ModelForm,TextInput
from .models import Expression

class ExpressionForm(ModelForm):
    
    class Meta:
        model = Expression
        fields='__all__'
        widgets={
            'title':TextInput(
                attrs={
                    'placeholder':'Enter title',
                    'class':'lchica'
                }
            ),
            'meaning':TextInput(
                attrs={
                    'placeholder':'Enter meaning',
                    'class':'lchica'
                }
            ),
            'example':TextInput(
                attrs={
                    'placeholder':'Enter example',
                    'class':'lchica'
                }
            )
        }