from unicodedata import name
from django.urls import path 
from users.views import home, register, directeur, chef_secteur, utilisateur

urlpatterns = [ 
    path('', home, name="home"),
    #path('accueil', accueil, name="accueil"),
    path('register', register, name='register'),
    path('directeur', directeur, name='directeur'),
    path('chef_secteur', chef_secteur, name='chef_secteur'),
    path('utilisateur', utilisateur, name='utilisateur'),
    #path('prediction', prediction, name='prediction'),
    
    path('logout_user', home, name="home"),
]
