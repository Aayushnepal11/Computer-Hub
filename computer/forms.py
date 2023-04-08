from django import forms
from .models import Computer, ComputerSpecification


class EditForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

class CreateData(forms.ModelForm):
    class Meta:
        model = ComputerSpecification
        fields = '__all__'
