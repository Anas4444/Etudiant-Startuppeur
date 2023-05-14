from django import forms
from django.contrib.auth.password_validation import validate_password
#from django.core import validators
#from django.contrib.auth import get_user_model
#from django.contrib.auth.forms import UserCreationForm
from .models import *
#from .validators import *


D = {'1': 'Physique',
     '2': 'Chimie',
     '3': 'Biologie', 
     '4': 'Mathématique', 
     '5': 'Informatique'}
E = {'1': '1ère année',
     '2': '2ème année',
     '3': '3ème année', 
     '4': '4ème année', 
     '5': '5ème année'}
class SignupForm(forms.ModelForm):
    '''password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    password_confirm = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])'''
    YOPTIONS = [
        ('1', '1ère année'),
        ('2', '2ème année'),
        ('3', '3ème année'), 
        ('4', '4ème année'), 
        ('5', '5ème année')
    ]
    DOPTIONS = [
        ('1', 'Physique'),
        ('2', 'Chimie'),
        ('3', 'Biologie'), 
        ('4', 'Mathématique'), 
        ('5', 'Informatique'),
        ('6', 'Autre')
    ]
    EOPTIONS = [
        ('1', 'Moi seul pour le moment'),
        ('2', '2 membres'),
        ('3', '3 membres'),
        ('4', '4 membres'),
        ('5', '5 membres')
    ]
    POPTIONS = [('0', 'Je n\'ai pas encore une idée de startup'),
                ('1', 'J\'ai une idée de startup')]

    other = forms.CharField(required=False)
    yearOfStudyOP = forms.ChoiceField(required=True, choices=YOPTIONS, initial='1')
    departementOP = forms.ChoiceField(required=True, choices=DOPTIONS, initial='5')
    ppOP = forms.ChoiceField(required=True, choices=POPTIONS, initial='1')
    equipeOP = forms.ChoiceField(required=False, choices=EOPTIONS, initial='1')

    class Meta:
        model = Participant
        fields = ['email', 'fullname', 'phone_number', 'faculte', 'specialite', 'skills', 'startupIdea']