from django.db import models

# Create your models here.
class Participant(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    faculte = models.CharField(max_length=50)
    specialite = models.CharField(max_length=50)
    departement = models.CharField(max_length=50)
    anneeEtude = models.CharField(max_length=50)
    skills = models.CharField(max_length=100, blank=True, null=True)
    porteurDeProjet = models.BooleanField()
    startupIdea = models.CharField(max_length=500, blank=True, null=True)
    equipe = models.IntegerField(blank=True, null=True)
    '''password = models.CharField(
        'Password hash',
        max_length=50)'''

    def __str__(self):
        return self.fullname