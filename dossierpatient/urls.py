from django.urls import path
from . import views

app_name = 'dossierpatient'



from django.urls import path
from .views import liste_centres

urlpatterns = [
    path('centres/', liste_centres, name='liste_centres'),


]



from django.urls import path
from .views import patient_list

urlpatterns = [
    path('patients/', patient_list, name='patient_list'),
]






from django.urls import path
from .views import liste_patriciens

urlpatterns = [
    path('patriciens/', liste_patriciens, name='liste_patriciens'),
]

urlpatterns = [


path('', views.dashboard, name='dashboard'),



]
