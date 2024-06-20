from django import forms
from .models import Block, Set


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = ['shape', 'color', 'size']


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['name', 'description', 'blocks']

