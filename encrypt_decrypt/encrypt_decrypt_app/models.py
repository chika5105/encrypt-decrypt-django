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
    image = models.ImageField(null=True, blank = True, upload_to= 'media')
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
    class Rank(models.TextChoices):
        CIPHER_LORD = 'Cipher Lord', _('Cipher Lord')
        SENIOR_CRYPTOGRAPHER = 'Senior Cryptographer', _('Senior Cryptographer')
        JUNIOR_CRYPTOGRAPHER = 'Junior Cryptographer', _('Junior Cryptographer')
        ANALYST = 'Analyst', _('Analyst')
        ROOKIE_ANALYST = 'Rookie Analyst', _('Rookie Analyst') 
    rank = models.CharField(max_length = 150,
    choices = Rank.choices,
    null = True,
    blank = True,
    default = Rank.ROOKIE_ANALYST)
    favorite_encryption = models.CharField( max_length = 150,
        choices = FavoriteEncryption.choices, 
        null = True,
        blank = True
    )
    messages = models.TextField(null = True, blank = True)
    def __str__(self):
        "String for representing the Model object"
        """if self.first_name and self.last_name:
            return f'{self.first_name}, {self.last_name}'
        else:
            return self.username
        """
        return self.username
    
    def get_absolute_url(self):
        "Returns url to access encryption scheme"
        return reverse('user-detail', args = [str(self.id)])
#TODO set messages as a separate model and foregin key to user


class CipherGame(models.Model):
    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'
    Impossible = 'Impossible'
    DIFFICULTY_LEVEL = [
        (Easy, 'Easy'),
        (Medium, 'Medium'),
        (Hard, 'Hard'),
        (Impossible, 'Impossible')
    ]
    difficulty = models.CharField(max_length = 30, 
    choices = DIFFICULTY_LEVEL,
    default = Easy,
    verbose_name = "Difficulty")
    name = models.CharField(max_length = 600, null = False, blank = False)
    cipher_text = models.TextField(null= False, blank = False)
    keys = models.TextField(null = True, blank = False)
    hint = models.TextField(null=True, blank = True)
    plain_text= models.TextField(null = False, blank = False)
    value = models.IntegerField()
    encryption_sequence = models.TextField(null=False, blank = False)
    encryptions_used = models.TextField(null = False, blank = False)
    solved = models.TextField(null = True, blank = True, default = 'None')

    def get_absolute_url(self):
        return reverse('cipher-game-detail', args = [str(self.id)])

    def __str__(self):
        return self.name

class Completed(models.Model):
    question_id = models.CharField(max_length = 600, null = True, blank = True)
    user_id = models.CharField(max_length= 600, null = True, blank = True)
    question_name = models.CharField(max_length = 1000, null = True, blank = True)
    user_name = models.CharField(max_length = 1000, null = True, blank = True)


    