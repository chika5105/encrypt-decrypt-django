from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Encryption(models.Model):
    CAESAR_CIPHER = 'Caesar Cipher'
    ATBASH_CIPHER = 'Atbash Cipher'
    VIGENERE_CIPHER = 'Vigenere Cipher'
    MORSE_CODE = 'Morse Code'
    NATO_CODE = 'NATO Code'
    REVERSE_CIPHER = 'Reverse Cipher'

    ENCRYPTION_CHOICES = [
        (CAESAR_CIPHER ,'Caesar Cipher'),
        (ATBASH_CIPHER , 'Atbash Cipher'),
        (VIGENERE_CIPHER, 'Vigenere Cipher'),
        (MORSE_CODE, 'Morse Code'),
        (NATO_CODE, 'NATO Code' ),
        (REVERSE_CIPHER, 'Reverse Cipher')

    ]
    encryption_technique = models.CharField(max_length=30,
     choices = ENCRYPTION_CHOICES,
     default = MORSE_CODE, 
     verbose_name= "Encryption Name"
     )
    description = models.TextField(null = True)
    def __str__(self):
        "String for representing the Model object"
        return self.encryption_technique
    
    def get_absolute_url(self):
        "Returns url to access encryption scheme"
        return reverse('encryption-detail', args = [str(self.id)])



# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, help_text = 'Enter your name')
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length = 100)
    message = models.TextField()
    def __str__(self):
        return f'{self.name}, {self.subject}'




class User(AbstractUser):
    score = models.IntegerField(default = 0, null = True, blank = True)
    #each user has a single favorite encryption but an encryption technique can be many people's favorite
    class FavoriteEncryption(models.TextChoices):
         CAESAR_CIPHER = 'CAESAR CIPHER', _('Caesar Cipher')
         ATBASH_CIPHER = 'ATBASH CIPHER',  _('Atbash Cipher')
         VIGENERE_CIPHER = 'VIGENERE CIPHER', _('Vigenere Cipher')
         MORSE_CODE = 'MORSE CODE', _('Morse Code')
         NATO_CODE = 'NATO CODE', _('Nato Code')
         REVERSE_CIPHER = 'REVERSE CIPHER', _('Reverse Cipher')
    favorite_encryption = models.CharField( max_length = 150,
        choices = FavoriteEncryption.choices, 
        null = True,
        blank = True
    )
    messages = models.TextField(null = True, blank = True)
    def __str__(self):
        "String for representing the Model object"
        if self.first_name and self.last_name:
            return f'{self.first_name}, {self.last_name}'
        else:
            return self.username
    
    def get_absolute_url(self):
        "Returns url to access encryption scheme"
        return reverse('user-detail', args = [str(self.id)])
