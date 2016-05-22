from django import forms

from models import Level


class UploadFileForm(forms.ModelForm):
    true = forms.ImageField()
    fake = forms.ImageField()

    class Meta:
        model = Level
        fields = ('true', 'fake',)

