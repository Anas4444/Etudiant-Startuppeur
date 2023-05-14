from email.message import EmailMessage
from django.shortcuts import render
from django.conf import settings
#from django.contrib.auth import login
from django.core.mail import EmailMessage
from .forms import *
from .models import *
import pygsheets
import pandas as pd

# Create your views here.
def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            #form.cleaned_data['password'] == form.cleaned_data['password_confirm']
            user = form.save(commit=False)
            if form.cleaned_data['departementOP']=='6' or len(form.cleaned_data['other'])>0:
                user.departement = form.cleaned_data['other']
            else:
                user.departement = D[form.cleaned_data['departementOP']]   
            user.anneeEtude = E[form.cleaned_data['yearOfStudyOP']]
            user.porteurDeProjet = bool(int(form.cleaned_data['ppOP']))
            user.equipe = int(form.cleaned_data['equipeOP'])
            user.save()
            data = []
            allP = Participant.objects.all()
            for p in allP:
                d = [p.fullname, p.email, p.phone_number, p.faculte, p.specialite, p.departement, p.anneeEtude, p.skills, p.porteurDeProjet, p.startupIdea, p.equipe]
                data.append(d)
            gc = pygsheets.authorize(service_file='staticfiles/creds.json')
            sh = gc.open('Participants')
            wks = sh[0]
            wks.set_dataframe(pd.DataFrame(data, columns = ['Full Name', 'E-Mail', 'Phone Number', 'Etablissement', 'Specialité', 'Departement', 'Year Of Study', 'compétences', 'Porteur de Projet', 'Startup Idea', 'Equipe']), (0,0))
            message = EmailMessage(
                'Registration',
                'Congratulations for your registration to ETUDIANT STARTUP-PEUR Event, \nYou just need to validate this form to complete your registration :\nhttps://forms.gle/BkXwy19FXU2oGaoZA\nThe event is hosted in this discord server join us using this link : \nhttps://discord.gg/MFC94Mbu',
                'fststartupnation@gmail.com',
                [user.email],
                headers={'Reply-To': 'fststartupnation@gmail.com'}
            )
            #message.attach_file('https://forms.gle/BkXwy19FXU2oGaoZA')
            message.send()
            return render(request, 'registration/validation.html')
        return render(request, 'registration/inscription.html', context={'form': form}) 
    return render(request, 'registration/inscription.html', context={'form': form})