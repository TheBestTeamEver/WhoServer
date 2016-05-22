from django import forms

from models import Level


class UploadFileForm(forms.ModelForm):
    name = forms.CharField()
    true_photo = forms.ImageField()
    fake_photo = forms.ImageField()

    class Meta:
        model = Level
        fields = ('name', 'true_photo', 'fake_photo',)

