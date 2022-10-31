import os

from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import (AboutForm, BarProgressForm, CardForm, MiniCardForm,
                    PersonalDataForm)
from .models import About, BarProgress, Card, MiniCard, PersonalData


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    minicards = MiniCard.objects.all()
    about = About.objects.all()[:1]
    barprogress = BarProgress.objects.all()
    cards = Card.objects.all()

    form_personaldata = PersonalDataForm
    form_minicard = MiniCardForm
    form_about = AboutForm
    form_barprogress = BarProgressForm
    form_card = CardForm

    context = {
        'personaldatas': personaldatas,
        'minicards': minicards,
        'about': about,
        'barprogress': barprogress,
        'cards': cards,

        'form_personaldata': form_personaldata,
        'form_minicard': form_minicard,
        'form_about': form_about,
        'form_barprogress': form_barprogress,
        'form_card': form_card,
    }
    return render(request, template_name, context)


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createpersonaldata(request):
    form = PersonalDataForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editpersonaldata(request):
    id = request.POST.get('personaldata_id')
    personaldata = PersonalData.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(personaldata.cover) > 0:
                os.remove(personaldata.cover.path)
            personaldata.cover = request.FILES['cover']
    personaldata.name = request.POST.get('name')
    personaldata.profession = request.POST.get('profession')
    personaldata.title = request.POST.get('title')
    personaldata.whatsapp = request.POST.get('whatsapp')
    personaldata.save()
    return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createsocialmedia(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editsocialmedia(request):
    id = request.POST.get('minicard_id')
    socialmedia = MiniCard.objects.get(id=id)

    if request.method == 'POST':
        socialmedia.name = request.POST.get('name')
        socialmedia.icon = request.POST.get('icon')
        socialmedia.link = request.POST.get('link')

        socialmedia.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deleteminicard(request, minicard_id):
    if not request.POST:
        raise Http404()

    minicard = MiniCard.objects.get(id=minicard_id)

    if not minicard:
        raise Http404()
    minicard.delete()

    return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createabout(request):
    form = AboutForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editabout(request):
    id = request.POST.get('about_id')
    aboutmedata = About.objects.get(id=id)
    if request.method == 'POST':
        aboutmedata.title = request.POST.get('title')
        aboutmedata.aboutme = request.POST.get('aboutme')

        aboutmedata.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createbarprogress(request):
    form = BarProgressForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editbarprogress(request):
    id = request.POST.get('barprogress_id')
    barprogress = BarProgress.objects.get(id=id)

    if request.method == 'POST':
        barprogress.title = request.POST.get('title')
        barprogress.progress = request.POST.get('progress')

        barprogress.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletebarprogress(request, barprogress_id):
    if not request.POST:
        raise Http404()

    barprogress = BarProgress.objects.get(id=barprogress_id)

    if not barprogress:
        raise Http404()
    barprogress.delete()

    return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createskills(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        skill = form.save(commit=False)
        skill.skills = True
        skill.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editskills(request):
    if request.method == 'POST':
        id = request.POST.get('minicard_id')
        name = request.POST.get('name')
        icon = request.POST.get('icon')
        link = request.POST.get('link')

        skills = MiniCard.objects.get(id=id)

        skills = MiniCard(
            id=id, name=name, icon=icon, link=link, skills=True)
        skills.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createcards(request):
    form = CardForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editcard(request):
    id = request.POST.get('card_id')
    card = Card.objects.get(id=id)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(card.cover) > 0:
                os.remove(card.cover.path)
            card.cover = request.FILES['cover']
        card.title = request.POST.get('title')
        card.subtitle = request.POST.get('subtitle')
        card.icon = request.POST.get('icon')
        card.linkgithub = request.POST.get('linkgithub')
        card.linkdeploy = request.POST.get('linkdeploy')
        card.datainfo = request.POST.get('datainfo')
        card.section = request.POST.get('section')

        card.save()
        return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletecard(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('card_id')

    card = Card.objects.get(id=id)

    if not card:
        raise Http404()

    card.delete()

    return redirect(reverse('portifolio:home'))
