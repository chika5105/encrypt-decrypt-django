from django.shortcuts import render, get_object_or_404
from .models import Encryption, Contact, User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from .forms import EncryptionForm, ContactForm, SignUpForm
from .caesar_cipher import CaesarCipher
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .atbash_cipher import AtbashCipher
from .reverse_cipher import ReverseCipher
from .vigenere_cipher import VigenereCipher
from .nato_code import NatoCode
from .morse_code import MorseCode




# Create your views here.
def index(request):
    """
    View function for HomePage
    """

    #counts number of time a user visits the homepage
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
        }
    return render(request, 'index.html', context = context)



@login_required
def encrypt_decrypt(request):
    form = EncryptionForm(request.GET)
    encryption_name = request.GET.get('encryption_name')
    if encryption_name:
        encryption_name= encryption_name.lower()
    message = request.GET.get('message')
    action = request.GET.get('action')
    if action:
        action = action.lower()
    key = request.GET.get('key')
    

    result = ""
    num_visits_encrypt = request.session.get('num_visits_encrypt', 0)
    request.session['num_visits_encrypt'] = num_visits_encrypt+ 1
    
    #TO DO CHECK LOGIC OF WHEN TO ENCRYPT AND DECREPT VERY CAREFULLY
    if form.is_valid():
        form = EncryptionForm()
        if action:
            if encryption_name == 'caesar cipher':
                result = encrypt_decrypt_caesar_cipher(message, action,key)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[0][0]
            #TODO handle encryption and fav
                if key:
                    form.fields['key'].initial = int(key)
                else:
                    form.fields['key'].initial = 20
            elif encryption_name == 'atbash cipher':
                form.fields['key'].hidden = True
                result = encrypt_decrypt_atbash_cipher(message)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[1][0]
            elif encryption_name == 'reverse cipher':
                form.fields['key'].hidden = True
                result = encrypt_decrypt_reverse_cipher(message)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[5][0]
            elif encryption_name == 'vigenere cipher':
                result = encrypt_decrypt_vigenere_cipher(message, action,key)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[2][0]
            elif encryption_name == 'morse code':
                result = encrypt_decrypt_morse_code(message,action)
                form.fields['result'].initial = result
                form.fields['key'].hidden = True
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[3][0]
            elif encryption_name == 'nato code':
                result = encrypt_decrypt_nato_code(message,action)
                form.fields['result'].initial = result
                form.fields['key'].hidden = True
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[4][0]
            form.fields['message'].initial = message
            context = {
                'form': form,
                'result': result,
                'num_visits_encrypt': num_visits_encrypt,
            }
            return render(request, 'encryption.html', context = context)

    context = {
        'form': form,
        'result': result,
        'num_visits_encrypt': num_visits_encrypt,
    }
    return render(request, 'encryption.html', context)

    
def encrypt_decrypt_caesar_cipher(message, action, key):
    caesar_cipher = CaesarCipher()
    if action == 'encrypt':
        if key:
            result = caesar_cipher.encrypt(message, int(key))
            return result
        else:
            result = caesar_cipher.encrypt(message) #user asked to encrypt message
            return result
    if action == 'decrypt':
        if key:
            result = caesar_cipher.decrypt(message, int(key))
            return result
        else:
            result = caesar_cipher.decrypt(message) #user asked to decrypt
            return result
def encrypt_decrypt_atbash_cipher(message):
    atbash_cipher = AtbashCipher()
    return atbash_cipher.encrypt(message)

def encrypt_decrypt_reverse_cipher(message):
    reverse_cipher = ReverseCipher()
    return reverse_cipher.encrypt(message)

def encrypt_decrypt_vigenere_cipher(message, action, key):
    vigenere_cipher = VigenereCipher()
    if action == 'encrypt':
        if key:
            result = vigenere_cipher.encrypt(message, (key))
            return result
        else:
            result = vigenere_cipher.encrypt(message) #user asked to encrypt message with default key
            return result
    if action == 'decrypt':
        if key:
            result = vigenere_cipher.decrypt(message,(key))
            return result
        else:
            result = vigenere_cipher.decrypt(message) #user asked to decrypt
            return result
def encrypt_decrypt_morse_code(message,action):
    morse_code = MorseCode()
    if action == 'encrypt':
        result = morse_code.encrypt(message)
    else:
        result = morse_code.decrypt(message)
    return result

def encrypt_decrypt_nato_code(message,action):
    nato_code = NatoCode()
    if action == 'encrypt':
        result = nato_code.encrypt(message)
    else:
        result = nato_code.decrypt(message)
    return result

def contact_me(request):
    contact = Contact()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.subject = form.cleaned_data['subject']
            contact.message = form.cleaned_data['message']
            contact.save()
            return render(request, 'contact_successful.html')
    else:
        form = ContactForm(request.GET)
    context = {
        'form': form,
        'contact': contact,
    }
    return render(request, 'contact_me.html', context= context)

class AboutListView(generic.ListView):
    model = Encryption
    context_object_name = 'encryption_list'
    template_name = 'about_list.html'

class AboutEncryptionView(generic.DetailView):
    model = Encryption
    context_object_name = 'encryption_detail'
    template_name = 'encryption_detail.html'

def sign_up(request):
    sign_up = User()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signup_successful.html')
    else:
        form = SignUpForm(request.GET)
    context = {
        'form': form,
        'signup': sign_up,
    }
    return render(request, 'sign_up.html', context= context)

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    context_object_name = 'user_detail'
    template_name = 'user_detail.html'
