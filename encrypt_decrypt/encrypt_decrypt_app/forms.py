from django import forms
from django.forms import ModelForm
from .models import Encryption, Contact, User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
encryption_choice = (
        (ENCRYPT ,'Encrypt'),
        (DECRYPT , 'Decrypt'),
)
class EncryptionForm(forms.Form):
    encryption_name = forms.ChoiceField(choices = Encryption.ENCRYPTION_CHOICES, required = True, label = 'Encryption Name', initial = Encryption.ENCRYPTION_CHOICES[2][1])
    #favorite = forms.ChoiceField(choices = Encryption.ENCRYPTION_CHOICES, required = False, label = 'Favorite Encryption?')
    key = forms.IntegerField(required = False, label = 'Key', help_text = 'Specify an integer custom key of your choice >= 0 or leave it blank to use the default key')
    action = forms.ChoiceField(choices = encryption_choice, widget= forms.RadioSelect,required = True)
    message = forms.CharField( widget = forms.Textarea, required = True, label = 'Message')
    result = forms.CharField(widget = forms.Textarea, required = False, disabled = True, label = "Result")
    def clean_message(self):
        data = self.cleaned_data['message']
        return data
    def clean_key(self):
        data = self.cleaned_data['key']
        if data is not None:
            if data < 0:
                raise ValidationError(_('Invalid key- key must be greater than or equal to 0'))
            return data
    def clean_result(self):
        data = self.cleaned_data['result']
        return data


class ContactForm(ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        return data
    def clean_email(self):
        data = self.cleaned_data['email']
        return data
    def clean_subject(self):
        data = self.cleaned_data['subject']
        return data
    def clean_message(self):
        data = self.cleaned_data['message']
        return data
    class Meta:
        model = Contact
        fields = '__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
    