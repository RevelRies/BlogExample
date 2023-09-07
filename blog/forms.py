from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='Еблонатор')
    age = forms.IntegerField(label='Возраст')
    gender = forms.NullBooleanField()