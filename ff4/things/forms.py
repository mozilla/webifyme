from django import forms
import re

class QuizForm(forms.Form):
    USERNAME_RE = re.compile(r'^[A-Za-z0-9_\'\-!\. ]+$')
    
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=False)
    download_reminder = forms.BooleanField(required=False)
    gallery_include = forms.BooleanField(required=False)
    
    def clean_username(self):
        if not self.USERNAME_RE.match(self.cleaned_data['username']):
            raise forms.ValidationError( _('Invalid characters in username') )
        return self.cleaned_data['username']
    
    def clean_download_reminder(self):
        if self.cleaned_data['download_reminder'] and not self.cleaned_data['email']:
            raise forms.ValidationError( _('Download reminder requires email.') )

class DownloadForm(forms.Form):
    email = forms.EmailField(required=False)
