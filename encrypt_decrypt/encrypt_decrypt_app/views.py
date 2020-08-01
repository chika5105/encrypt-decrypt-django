from django.shortcuts import render, get_object_or_404
from .models import Encryption, Contact, User, CipherGame, Completed
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .forms import EncryptionForm, ContactForm, SignUpForm, CipherGameForm
from .caesar_cipher import CaesarCipher
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .atbash_cipher import AtbashCipher
from .reverse_cipher import ReverseCipher
from .vigenere_cipher import VigenereCipher
from .nato_code import NatoCode
from .morse_code import MorseCode
from .has_seen_object import check as check
import random
from django.core.mail import send_mail, BadHeaderError
from encrypt_decrypt.settings import EMAIL_HOST_USER
from django.core.cache import cache






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
    if key:
        key = key.strip()
    

    result = ""
    num_visits_encrypt = request.session.get('num_visits_encrypt', 0)
    request.session['num_visits_encrypt'] = num_visits_encrypt+ 1
    
    #TO DO CHECK LOGIC OF WHEN TO ENCRYPT AND DECREPT VERY CAREFULLY
    if form.is_valid():
        form = EncryptionForm()
        if action:
            if encryption_name == 'caesar cipher':
                if key.isnumeric():
                    result = encrypt_decrypt_caesar_cipher(message, action,int(key))
                else:
                    result = encrypt_decrypt_caesar_cipher(message,action, None)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[0][0]
                form.fields['action'].initial = action
                if key and key.isnumeric():
                    form.fields['key'].initial = str(key)
                else:
                    form.fields['key'].initial = str(20)
            elif encryption_name == 'atbash cipher':
                result = encrypt_decrypt_atbash_cipher(message)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[1][0]
                form.fields['action'].initial = action
            elif encryption_name == 'reverse cipher':
                result = encrypt_decrypt_reverse_cipher(message)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[5][0]
                form.fields['action'].initial = action
            elif encryption_name == 'vigenere cipher':
                if key.isalpha():
                    if len(key)>=len(message):
                        result = encrypt_decrypt_vigenere_cipher(message, action,key)
                    else:
                        result = encrypt_decrypt_vigenere_cipher(message,action,None)
                else:
                    result = encrypt_decrypt_vigenere_cipher(message,action, None)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[2][0]
                form.fields['action'].initial = action
                if key and key.isalpha():
                    form.fields['key'].initial = str(key)
                else:
                    form.fields['key'].initial = 'z' * len(message)
               
            elif encryption_name == 'morse code':
                result = encrypt_decrypt_morse_code(message,action)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[3][0]
                form.fields['action'].initial = action
            elif encryption_name == 'nato code':
                result = encrypt_decrypt_nato_code(message,action)
                form.fields['result'].initial = result
                form.fields['encryption_name'].initial = Encryption.ENCRYPTION_CHOICES[4][0]
                form.fields['action'].initial = action
            form.fields['message'].initial = message
            context = {
                'form': form,
                'result': result,
                'num_visits_encrypt': num_visits_encrypt,
            }
            return render(request, 'encryption_engine.html', context = context)

    context = {
        'form': form,
        'result': result,
        'num_visits_encrypt': num_visits_encrypt,
    }
    return render(request, 'encryption_engine.html', context=context)

    
def encrypt_decrypt_caesar_cipher(message, action, key):
    caesar_cipher = CaesarCipher()
    if action == 'encrypt':
        if key:
            result = caesar_cipher.encrypt(message, int(key))
            return result
        else:
            result = caesar_cipher.encrypt(message) #user asked to encrypt message with default key
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
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.subject = form.cleaned_data['subject']
            contact.message = form.cleaned_data['message']
            contact.image = form.cleaned_data['image']
            contact.save()
            send_email = form.cleaned_data['send_email']
       
            subject = "Contact Form Copy"
            message = 'Hey '+ contact.name + ". You asked for a copy of your message in the contact form. If this wasn't you, kindly ignore this message. You can find your message below:" + "\n"+ "Subject: " + contact.subject + "\n" + "Message: " + contact.message + "\n" + "Kind regards," + "\n" + "Chika's Cipher Website"
            recipient = contact.email
            from_email = EMAIL_HOST_USER
            if send_email:
                if subject and message and from_email:
                    try:
                        send_mail(subject, message, from_email, [str(recipient)])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
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
    template_name = 'encryption_list.html'

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

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user_form.html'
    fields=['first_name', 'last_name', 'email', 'username','favorite_encryption']
    success_url = reverse_lazy('user-update-success') #TODO change this

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user-delete-success')

def user_delete_success(request):
    context = {

    }
    return render(request, 'user_delete_success.html', context = context)

def user_update_success(request):
    context = {

    }
    return render(request, 'user_update_success.html', context = context)

class CipherGameListView(generic.ListView):
    model = CipherGame
    context_object_name = 'cipher_game_list'
    template_name = 'cipher_game_list.html'
    
@cache_page(60*15)
@login_required
def solve_game(request, pk):
    #TODO add Question Name to html
    cur_user = User.objects.get(pk = request.user.pk)
    question = CipherGame.objects.get(pk = pk)
    form = CipherGameForm()
    form.fields['cipher_text'].initial = question.cipher_text
    form.fields['keys'].initial = question.keys
    form.fields['hint'].initial = question.hint
    if question.difficulty.lower() == 'easy':
        form.fields['encryptions_used'].widget = forms.HiddenInput()
    else:
        form.fields['encryptions_used'].initial = question.encryptions_used
    request.GET.get(form)
    plain_text = request.GET.get('plain_text')
    see_ans = request.GET.get('see_ans')
    message = ""
    alert = ""
    rank_update = ""
    title = 'Correct, Way to go ' + str(cur_user.rank)+'!'
    message_success = random.choice(['Congratulations! You made that look easy!', 'Correct!', title, 'Well done!'])
    message_wrong = random.choice(['Sorry, wrong answer try again! ', 'Incorrect, try again. ', "That was wrong, try again. "]) + random.choice([ "Failure isn't fatal, but failure to change might be-James Wooden", "Only those who dare to fail greatly can ever achieve greatly-Robert F. Kennedy", "Success is most often achieved by those who don't know that failure is inevitable. - Coco Chanel","The phoenix must burn to emerge. - Janet Fitch" , "Giving up is the only sure way to fail. - Gena Showalter", "Pain is temporary, quitting lasts forever-Lance Armstrong", "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela" ])
    message_ans = random.choice(["Phew! Wasn't that intense! Better luck next time", "You've tried your best, but sometimes our best isn't enough", "Of all the words of mice and men, the saddest are, 'It might have been'-Kurt Vonnegut", "Hindsight Vision is always 20/20"])
    
    if see_ans:
        
            form = CipherGameForm(request.GET)
            form.fields['cipher_text'].initial = question.cipher_text
            form.fields['plain_text'].initial = question.plain_text
            form.fields['plain_text'].disabled = True
            form.fields['plain_text'].label = 'Correct Answer'
            form.fields['encryptions_used'].initial = question.encryption_sequence
            form.fields['encryptions_used'].label = 'Encryptions Used'
            form.fields['keys'].initial = question.keys
            form.fields['hint'].initial = question.hint
            check.insert(question.pk, cur_user.pk)
            answered = Completed()
            answered.question_id = question.pk
            answered.user_id = cur_user.pk
            answered.user_name = cur_user.username
            answered.question_name = question.name
            answered.save()

            message = message_ans
            alert = 'ans'
            context = {
                'form': form,
                'message': message,
                'alert': alert,
                'rank_update': rank_update
            }
            return render(request, 'cipher_game_detail.html', context = context)
    if not check.has_seen(question.pk, cur_user.pk):
        if plain_text:
            if is_correct(plain_text, question.plain_text):
                alert = 'success'
                if cur_user.score is not None:
                    cur_user.score+=question.value
                else:
                    cur_user.score = question.value
                old_rank = cur_user.rank
                if cur_user.score>= 20:
                    cur_user.rank = User.Rank.ANALYST
                if cur_user.score >= 40:
                     cur_user.rank = User.Rank.JUNIOR_CRYPTOGRAPHER
                if cur_user.score >= 90:
                    cur_user.rank = User.Rank.SENIOR_CRYPTOGRAPHER
                if cur_user.score >=140:
                    cur_user.rank = User.Rank.CIPHER_LORD
                check.insert(question.pk, cur_user.pk)
                back_up = Completed()
                back_up.question_id = question.pk
                back_up.user_id = cur_user.pk
                back_up.user_name = cur_user.username
                back_up.question_name = question.name
                back_up.save()
                question.solved += (' ' + str(cur_user.username) + ' , ')
                question.save()
                cur_user.save()
                message = message_success
                if cur_user.rank!=old_rank:
                    rank_update = "Congratulations! You've earned a new rank. You're now a " + str(cur_user.rank) + '!'

            else:
                message = message_wrong
                alert = 'wrong'
    else:
        if plain_text:
            if is_correct(plain_text, question.plain_text):
                message = message_success
                alert = 'success'
            else:
                message = message_wrong
                alert = 'wrong'
                
    context = {
    'form': form,
    'message': message,
    'alert': alert,
    'rank_update': rank_update
    }
    return render(request, 'cipher_game_detail.html', context = context)
   


  
    
def is_correct(user_input, answer_key):
    return user_input.strip().lower() == answer_key.strip().lower()


def leaderboard(request):
    query_set = User.objects.order_by('-score')[:10]
    context = {
    'query_set': query_set,
    }
    return render(request, 'leaderboard.html', context = context)

@cache_page(60*15)
def instructions(request):
    num_visits_instructions = request.session.get('num_visits_instructions', 0)
    request.session['num_visits_instructions'] = num_visits_instructions + 1
    context = {
        'num_visits_instructions': num_visits_instructions,
    }
    return render(request, 'instructions.html', context = context)