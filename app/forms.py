from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['task', 'category', 'memo', 'start_day', 'end_day', 'start_time','end_time', 'completed']
        widgets = {
                    'task': forms.TextInput(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                    'completed':forms.CheckboxInput(),
                    'category':forms.Select(attrs={'choices':'CATEGORY_CHOICES'}),
                    'start_day':forms.DateInput(attrs={'type': 'date',"format": "yyyy/mm/dd/",}),
                    'end_day':forms.DateInput(attrs={'type': 'date', "format": "yyyy/mm/dd/",}),
                    'start_time':forms.TimeInput(attrs={'type': 'time',"format": "hh:mm",}),
                    'end_time':forms.TimeInput(attrs={'type': 'time',"format": "hh:mm"}),
        }