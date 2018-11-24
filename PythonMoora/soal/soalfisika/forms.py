from django import forms
from orm.models import HasilTes


class HasilTesForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    mata_pelajaran = forms.CharField(max_length=30)
    nilai = forms.CharField(max_length=30)

    class Meta:
        model = HasilTes
