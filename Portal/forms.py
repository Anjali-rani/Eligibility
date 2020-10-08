from django import forms
from Portal.models import *
from . import models


class Choice(forms.ModelForm):
    class Meta:
        model = models.Questions
        fields = ['category']




