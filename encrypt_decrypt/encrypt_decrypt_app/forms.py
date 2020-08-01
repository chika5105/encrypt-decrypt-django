from django import forms
from django.forms import ModelForm
from .models import Encryption, Contact, User, CipherGame
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
encryption_choice = (
        (ENCRYPT ,'Encrypt'),
        (DECRYPT , 'Decrypt'),
)
class EncryptionForm(forms.Form):
    encryption_name = forms.ChoiceField(choices = Encryption.ENCRYPTION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),required = True, label = 'Encryption Name', initial = Encryption.ENCRYPTION_CHOICES[2][1])
    key = forms.CharField(required = False, label = 'Key', widget = forms.TextInput(attrs= {'class': 'form-control', }))
    action = forms.ChoiceField(choices = encryption_choice, widget= forms.RadioSelect(attrs= {'class': 'form-check-label', 'type': 'radio'}),required = True)
    message = forms.CharField( widget = forms.Textarea(attrs={'rows': 3, 'cols':20, 'class':'form-control'}), required = True, label = 'Message')
    result = forms.CharField(widget = forms.Textarea(attrs={'rows':3, 'cols': 20, 'class':'form-control'}), required = False, disabled = True, label = "Result")
    def clean_message(self):
        data = self.cleaned_data['message']
        return data
    def clean_key(self):
        data = self.cleaned_data['key']
        if data is not None and data.isnumeric():
            data = int(data)
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
    def clean_image(self):
        data = self.cleaned_data['image']
        return data
    def clean_send_email(self):
        data = self.cleaned_data['send_email']
        return data
    class Meta:
        model = Contact
        labels = {'image': _('Upload Image')}
        help_texts = {'image': _('Please upload only immage files')} 
        fields = '__all__'
    choice = [('Yes', 'Email Me A Copy of My Message')]
    #send_email = forms.ChoiceField(widget = forms.CheckboxSelectMultiple, choices = choice, required= False)
    send_email = forms.BooleanField(required = False, label = 'Email Me A Copy of My Message')

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']



class CipherGameForm(forms.Form):
    YES = 'Yes'
    see_ans_choices = (
        (YES, 'Yes pls!'),
    )
    cipher_text = forms.CharField(disabled = True, label = 'Ciphertext', widget = forms.Textarea(attrs={'rows': 2, 'cols':20}))
    keys = forms.CharField(label = 'Keys Used', disabled= True, widget = forms.Textarea(attrs={'rows': 2, 'cols':20}), help_text= mark_safe("Use these keys to decrypt the cipher text. Note that the order you use the keys determine if you'll be successful or not"))
    plain_text = forms.CharField(label = 'Plaintext', required = False, widget = forms.Textarea(attrs={'rows': 2, 'cols':20}))
    hint = forms.CharField(label= 'Hint', disabled = True, required= False,widget = forms.Textarea(attrs={'rows': 2, 'cols':20}))
    see_ans = forms.ChoiceField(choices = see_ans_choices, widget=forms.CheckboxSelectMultiple, required = False)
    encryptions_used = forms.CharField( widget = forms.Textarea(attrs={'rows': 3, 'cols':20}),disabled = True, required = False)
    

    def clean_cipher_text(self):
        data = self.cleaned_data['cipher_text']
        return data
    
    def clean_keys(self):
        data = self.cleaned_data['keys']
        return data

    def clean_plain_text(self):
        data = self.cleaned_data['plain_text']
        return data

    def clean_hint(self):
        data = self.cleaned_data['hint']
        return data

    def clean_see_as(self):
        data = self.cleaned_data['see_ans']
        return data

    def clean_encryptions_used(self):
        data = self.cleaned_data['encryptions_used']
        return data


    