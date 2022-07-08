from django import forms
#from .models import Unnes
from .models import UserInput

'''
class UnnesForm(forms.ModelForm):
    class Meta:
        model = Unnes     #создание формы под модель
        fields = [
            'title',
            'description',
            'price',
        ]
'''
class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = [
        'sometxt',
        ]
