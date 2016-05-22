from django import forms

from models import Level


class UploadFileForm(forms.ModelForm):
    true_name = forms.CharField(max_length=64)
    true_photo = forms.ImageField()
    fake_name = forms.CharField(max_length=64)
    fake_photo = forms.ImageField()

    class Meta:
        model = Level
        fields = ('true_name', 'true_photo', 'fake_name', 'fake_photo',)

