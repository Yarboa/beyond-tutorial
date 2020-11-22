from django import forms
from msgboard.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('author', 'text')
