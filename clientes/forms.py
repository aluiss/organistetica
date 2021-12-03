from django import forms
from django.forms import widgets
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

    """ def __init__(self, *args, **kwargs):
        super(AnamneseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control-sm' """