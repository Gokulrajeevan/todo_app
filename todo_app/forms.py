from django import forms

from todo_app.models import Task


class Taskform(forms.ModelForm):
    class Meta:
        model=Task;
        fields=['name','priority','date']

