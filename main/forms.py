from PIL.ImageChops import multiply
from django import forms
from django.contrib.auth.models import User
from .models import Spect



class SpectForm(forms.ModelForm):

    class Meta:
        model = Spect
        fields = ('name', 'link', 'length')
        widgets = {
            'video': forms.FileInput(attrs={'multiply': 'True'}),
        }


# class SpectAddForm(forms.ModelForm):
#
#     class Meta:
#         model = Spect
#         fields = ('name', 'link', 'length', 'video', 'svet_doc', 'zvuk_doc', 'video_doc', 'decor_doc', 'rekv_doc', 'grim_doc', 'kostum_doc')
#         widgets = {
#             'video': forms.FileInput(attrs={'multiply': 'True'}),
#         }