from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('vente', views.vente, name='vente'),
    path('maison_passage', views.passe, name='maison_passage'),
    path('parcelle', views.parce, name='parcelle'),
    path('four', views.fourroom, name='four'),
    path('three', views.threeroom, name='three'),
    path('two', views.tworoom, name='two'),
    path('one', views.oneroom, name='one'),
    path('details/<id>', views.details, name="details"),
]
