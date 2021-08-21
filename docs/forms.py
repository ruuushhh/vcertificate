
from django import forms

activity_choice = [
    ('curriculam', 'Curriculam'),
    ('extra Co-curriculam', 'Extra Co-Curriculam')
]


class Upload_form(forms.Form):
    file_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    file_description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    file_activity = forms.CharField(widget=forms.RadioSelect(
        choices=activity_choice))
    file_year = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
