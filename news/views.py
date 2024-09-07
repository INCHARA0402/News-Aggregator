from django.shortcuts import render, redirect
import requests
import json
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages

@login_required(login_url='login')
def home(request):
    news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    api = json.loads(news_api.content)
    return render(request, 'home.html', {'api': api})

@login_required(login_url='login')
def bnews(request):
    b_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    b_api = json.loads(b_news_api.content)
    return render(request, 'bnews.html', {'b_api': b_api})

@login_required(login_url='login')
def enews(request):
    e_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    e_api = json.loads(e_news_api.content)
    return render(request, 'enews.html', {'e_api': e_api})

@login_required(login_url='login')
def hnews(request):
    h_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    h_api = json.loads(h_news_api.content)
    return render(request, 'hnews.html', {'h_api': h_api})

@login_required(login_url='login')
def scnews(request):
    sc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    sc_api = json.loads(sc_news_api.content)
    return render(request, 'scnews.html', {'sc_api': sc_api})

@login_required(login_url='login')
def snews(request):
    s_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    s_api = json.loads(s_news_api.content)
    return render(request, 'snews.html', {'s_api': s_api})

@login_required(login_url='login')
def tnews(request):
    t_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    t_api = json.loads(t_news_api.content)
    return render(request, 'tnews.html', {'t_api': t_api})

@login_required(login_url='login')
def canews(request):
    ca_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    ca_api = json.loads(ca_news_api.content)
    return render(request, 'canews.html', {'ca_api': ca_api})

@login_required(login_url='login')
def aunews(request):
    au_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    au_api = json.loads(au_news_api.content)
    return render(request, 'aunews.html', {'au_api': au_api})

@login_required(login_url='login')
def frnews(request):
    fr_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    fr_api = json.loads(fr_news_api.content)
    return render(request, 'frnews.html', {'fr_api': fr_api})

@login_required(login_url='login')
def krnews(request):
    kr_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    kr_api = json.loads(kr_news_api.content)
    return render(request, 'krnews.html', {'kr_api': kr_api})
@login_required(login_url='login')
def thnews(request):
    th_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    th_api = json.loads(th_news_api.content)
    return render(request, 'thnews.html', {'th_api': th_api})

@login_required(login_url='login')
def itnews(request):
    it_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    it_api = json.loads(it_news_api.content)
    return render(request, 'itnews.html', {'it_api': it_api})

@login_required(login_url='login')
def cabnews(request):
    cab_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    cab_api = json.loads(cab_news_api.content)
    return render(request, 'cabnews.html', {'cab_api': cab_api})

@login_required(login_url='login')
def aubnews(request):
    aub_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    aub_api = json.loads(aub_news_api.content)
    return render(request, 'aubnews.html', {'aub_api': aub_api})

@login_required(login_url='login')
def frbnews(request):
    frb_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    frb_api = json.loads(frb_news_api.content)
    return render(request, 'frbnews.html', {'frb_api': frb_api})

@login_required(login_url='login')
def krbnews(request):
    krb_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    krb_api = json.loads(krb_news_api.content)
    return render(request, 'krbnews.html', {'krb_api': krb_api})

@login_required(login_url='login')
def thbnews(request):
    thb_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    thb_api = json.loads(thb_news_api.content)
    return render(request, 'thbnews.html', {'thb_api': thb_api})

@login_required(login_url='login')
def itbnews(request):
    itb_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=business&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    itb_api = json.loads(itb_news_api.content)
    return render(request, 'itbnews.html', {'itb_api': itb_api})

@login_required(login_url='login')
def caenews(request):
    cae_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    cae_api = json.loads(cae_news_api.content)
    return render(request, 'caenews.html', {'cae_api': cae_api})

@login_required(login_url='login')
def auenews(request):
    aue_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    aue_api = json.loads(aue_news_api.content)
    return render(request, 'auenews.html', {'aue_api': aue_api})

@login_required(login_url='login')
def frenews(request):
    fre_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    fre_api = json.loads(fre_news_api.content)
    return render(request, 'frenews.html', {'fre_api': fre_api})

@login_required(login_url='login')
def krenews(request):
    kre_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    kre_api = json.loads(kre_news_api.content)
    return render(request, 'krenews.html', {'kre_api': kre_api})

@login_required(login_url='login')
def thenews(request):
    the_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    the_api = json.loads(the_news_api.content)
    return render(request, 'thenews.html', {'the_api': the_api})

@login_required(login_url='login')
def itenews(request):
    ite_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=entertainment&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    ite_api = json.loads(ite_news_api.content)
    return render(request, 'itenews.html', {'ite_api': ite_api})

@login_required(login_url='login')
def cahnews(request):
    cah_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    cah_api = json.loads(cah_news_api.content)
    return render(request, 'cahnews.html', {'cah_api': cah_api})

@login_required(login_url='login')
def auhnews(request):
    auh_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    auh_api = json.loads(auh_news_api.content)
    return render(request, 'auhnews.html', {'auh_api': auh_api})

@login_required(login_url='login')
def frhnews(request):
    frh_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    frh_api = json.loads(frh_news_api.content)
    return render(request, 'frhnews.html', {'frh_api': frh_api})

@login_required(login_url='login')
def krhnews(request):
    krh_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    krh_api = json.loads(krh_news_api.content)
    return render(request, 'krhnews.html', {'krh_api': krh_api})

@login_required(login_url='login')
def thhnews(request):
    thh_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    thh_api = json.loads(thh_news_api.content)
    return render(request, 'thhnews.html', {'thh_api': thh_api})

@login_required(login_url='login')
def ithnews(request):
    ith_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=health&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    ith_api = json.loads(ith_news_api.content)
    return render(request, 'ithnews.html', {'ith_api': ith_api})

@login_required(login_url='login')
def cascnews(request):
    casc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    casc_api = json.loads(casc_news_api.content)
    return render(request, 'cascnews.html', {'casc_api': casc_api})

@login_required(login_url='login')
def auscnews(request):
    ausc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    ausc_api = json.loads(ausc_news_api.content)
    return render(request, 'auscnews.html', {'ausc_api': ausc_api})

@login_required(login_url='login')
def frscnews(request):
    frsc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    frsc_api = json.loads(frsc_news_api.content)
    return render(request, 'frscnews.html', {'frsc_api': frsc_api})

@login_required(login_url='login')
def krscnews(request):
    krsc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    krsc_api = json.loads(krsc_news_api.content)
    return render(request, 'krscnews.html', {'krsc_api': krsc_api})

@login_required(login_url='login')
def thscnews(request):
    thsc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    thsc_api = json.loads(thsc_news_api.content)
    return render(request, 'thscnews.html', {'thsc_api': thsc_api})

@login_required(login_url='login')
def itscnews(request):
    itsc_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=science&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    itsc_api = json.loads(itsc_news_api.content)
    return render(request, 'itscnews.html', {'itsc_api': itsc_api})

@login_required(login_url='login')
def casnews(request):
    cas_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    cas_api = json.loads(cas_news_api.content)
    return render(request, 'casnews.html', {'cas_api': cas_api})

@login_required(login_url='login')
def ausnews(request):
    aus_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    aus_api = json.loads(aus_news_api.content)
    return render(request, 'ausnews.html', {'aus_api': aus_api})

@login_required(login_url='login')
def frsnews(request):
    frs_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    frs_api = json.loads(frs_news_api.content)
    return render(request, 'frsnews.html', {'frs_api': frs_api})

@login_required(login_url='login')
def krsnews(request):
    krs_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    krs_api = json.loads(krs_news_api.content)
    return render(request, 'krsnews.html', {'krs_api': krs_api})

@login_required(login_url='login')
def thsnews(request):
    ths_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    ths_api = json.loads(ths_news_api.content)
    return render(request, 'thsnews.html', {'ths_api': ths_api})

@login_required(login_url='login')
def itsnews(request):
    its_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=sports&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    its_api = json.loads(its_news_api.content)
    return render(request, 'itsnews.html', {'its_api': its_api})

@login_required(login_url='login')
def catnews(request):
    cat_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=ca&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    cat_api = json.loads(cat_news_api.content)
    return render(request, 'catnews.html', {'cat_api': cat_api})

@login_required(login_url='login')
def autnews(request):
    aut_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=au&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    aut_api = json.loads(aut_news_api.content)
    return render(request, 'autnews.html', {'aut_api': aut_api})

@login_required(login_url='login')
def frtnews(request):
    frt_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    frt_api = json.loads(frt_news_api.content)
    return render(request, 'frtnews.html', {'frt_api': frt_api})

@login_required(login_url='login')
def krtnews(request):
    krt_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=kr&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    krt_api = json.loads(krt_news_api.content)
    return render(request, 'krtnews.html', {'krt_api': krt_api})

@login_required(login_url='login')
def thtnews(request):
    tht_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=th&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    tht_api = json.loads(tht_news_api.content)
    return render(request, 'thtnews.html', {'tht_api': tht_api})

@login_required(login_url='login')
def ittnews(request):
    itt_news_api = requests.get(
        "http://newsapi.org/v2/top-headlines?country=it&category=technology&apiKey=abb8f9ed762842c7aa2f892dd8b8f37a")
    itt_api = json.loads(itt_news_api.content)
    return render(request, 'ittnews.html', {'itt_api': itt_api})
