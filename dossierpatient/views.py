

from django.shortcuts import render









# Create your views here.


def liste_centres(request):
    liste_centres = liste_centres.objects.all()
    return render(request, 'liste_centres.html', {'liste_centres': liste_centres})


from django.shortcuts import render
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})


from django.shortcuts import render
from .models import Patricien

def liste_patriciens(request):
    patriciens = Patricien.objects.all()
    return render(request, 'liste_patriciens.html', {'patriciens': patriciens})



def dashboard(request, *args, **kwargs):

    return render(request,  'index.html')