from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def accueil(request):
    return render(request, 'index.html')

def vente(request):
    four_list = House.objects.all()

    p = Paginator(House.objects.all(), 3)
    page = request.GET.get('page')
    four_lists = p.get_page(page)
    nums = "a" * four_lists.paginator.num_pages

    context = {'four_list':four_list, 'four_lists':four_lists, 'nums':nums}
    return render(request, 'vente.html', locals())

def passe(request):
    return render(request, 'pass.html')

def parce(request):
    return render(request, 'parc.html')

def fourroom(request):
    four_list = House.objects.all()

    p = Paginator(House.objects.all(), 3)
    page = request.GET.get('page')
    four_lists = p.get_page(page)
    nums = "a" * four_lists.paginator.num_pages

    context = {'four_list':four_list, 'four_lists':four_lists, 'nums':nums}
    return render(request, 'accueil.html', context)


def threeroom(request):
    three_list = House.objects.all()

    p = Paginator(House.objects.all(), 3)
    page = request.GET.get('page')
    three_lists = p.get_page(page)
    nums = "a" * three_lists.paginator.num_pages

    context = {'three_list':three_list, 'three_lists':three_lists, 'nums':nums}
    return render(request, 'accueil3.html', context)


def tworoom(request):
    four_list = House.objects.all()

    p = Paginator(House.objects.all(), 3)
    page = request.GET.get('page')
    four_lists = p.get_page(page)
    nums = "a" * four_lists.paginator.num_pages

    context = {'four_list':four_list, 'four_lists':four_lists, 'nums':nums}
    return render(request, 'accueil2.html', context)

def oneroom(request):
    four_list = House.objects.all()

    p = Paginator(House.objects.all(), 3)
    page = request.GET.get('page')
    four_lists = p.get_page(page)
    nums = "a" * four_lists.paginator.num_pages

    context = {'four_list':four_list, 'four_lists':four_lists, 'nums':nums}
    return render(request, 'accueil1.html', context)

def details(request, id):
    ho = House.objects.filter(number=id)
    return render(request, 'details.html', {'ho':ho})