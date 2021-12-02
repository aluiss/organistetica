from django import forms
from clientes.models import Anamnese

class AnamneseForm(forms.ModelForm):
    altura = forms.FloatField()
    peso = forms.FloatField()
    fumante = forms.BooleanField()
    bebe = forms.BooleanField()

    class Meta:
        model = Anamnese
        #exclude = ['cliente',]
        fields = ['altura', 'peso', 'fumante', 'bebe']