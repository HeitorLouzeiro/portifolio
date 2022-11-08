import os

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import (AboutForm, BarProgressForm, CardForm, MiniCardForm,
                    PersonalDataForm)
from .models import About, BarProgress, Card, MiniCard, PersonalData


# url dinamicas
def url_home():
    url = redirect(reverse('portifolio:home')+f'#home')  # noqa
    return url


def url_about():
    url = redirect(reverse('portifolio:home')+f'#about')  # noqa
    return url


def url_curriculum():
    url = redirect(reverse('portifolio:home')+f'#curriculo')  # noqa
    return url


def url_services():
    url = redirect(reverse('portifolio:home')+f'#services')  # noqa
    return url


def url_portfolio():
    url = redirect(reverse('portifolio:home')+f'#portfolio')  # noqa
    return url


def url_contact():
    url = redirect(reverse('portifolio:home')+f'#contact')  # noqa
    return url


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
        return url_home()


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
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createsocialmedia(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        form.save()
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editsocialmedia(request):
    id = request.POST.get('minicard_id')
    socialmedia = MiniCard.objects.get(id=id)

    if request.method == 'POST':
        socialmedia.name = request.POST.get('name')
        socialmedia.icon = request.POST.get('icon')
        socialmedia.link = request.POST.get('link')

        socialmedia.save()
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deleteminicard(request, minicard_id):
    if not request.POST:
        raise Http404()

    minicard = MiniCard.objects.get(id=minicard_id)

    if not minicard:
        raise Http404()
    if minicard.skills is False:
        minicard.delete()
        return url_home()
    else:
        minicard.delete()
        return url_curriculum()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createabout(request):
    form = AboutForm(request.POST or None)

    if form.is_valid():
        form.save()
        return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editabout(request):
    id = request.POST.get('about_id')
    aboutmedata = About.objects.get(id=id)
    if request.method == 'POST':
        aboutmedata.title = request.POST.get('title')
        aboutmedata.aboutme = request.POST.get('aboutme')

        aboutmedata.save()
        return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createbarprogress(request):
    form = BarProgressForm(request.POST or None)

    if form.is_valid():
        form.save()
        return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editbarprogress(request):
    id = request.POST.get('barprogress_id')
    barprogress = BarProgress.objects.get(id=id)

    if request.method == 'POST':
        barprogress.title = request.POST.get('title')
        barprogress.progress = request.POST.get('progress')

        barprogress.save()
        return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletebarprogress(request, barprogress_id):
    if not request.POST:
        raise Http404()

    barprogress = BarProgress.objects.get(id=barprogress_id)

    if not barprogress:
        raise Http404()
    barprogress.delete()

    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createskills(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        skill = form.save(commit=False)
        skill.skills = True
        skill.save()
        return url_curriculum()


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
        return url_curriculum()


def redirect_action_card(card, cardaction):
    if cardaction is True:
        if card.section == '1':
            card.save()
            return url_about()
        elif card.section == '2':
            card.save()
            return url_curriculum()
        elif card.section == '3':
            card.save()
            return url_services()
        elif card.section == '4':
            card.save()
            return url_portfolio()
        else:
            return redirect(reverse('portifolio:home'))
    else:
        if card.section == '1':
            card.delete()
            return url_about()
        elif card.section == '2':
            card.delete()
            return url_curriculum()
        elif card.section == '3':
            card.delete()
            return url_services()
        elif card.section == '4':
            card.delete()
            return url_portfolio()
        else:
            return redirect(reverse('portifolio:home'))


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createcards(request):
    form = CardForm(request.POST, request.FILES or None)

    if form.is_valid():
        card = form.save(commit=False)
        cardaction = True
        return redirect_action_card(card, cardaction)


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
        cardaction = True
        return redirect_action_card(card, cardaction)


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletecard(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('card_id')

    card = Card.objects.get(id=id)

    if not card:
        raise Http404()

    cardaction = False
    return redirect_action_card(card, cardaction)


def sendemail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', [
                  'heitorlouzeirodev@gmail.com'])
    return url_contact()
