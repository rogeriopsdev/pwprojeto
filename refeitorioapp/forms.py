from refeitorioapp.models import Mesa
from django import forms

class MesaForms(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"