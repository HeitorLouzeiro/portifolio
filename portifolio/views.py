from django.http import HttpResponse
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


def createpersonaldata(request):
    form = PersonalDataForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


def editpersonaldata(request):
    if request.method == 'POST':
        id = request.POST.get('personaldata_id')
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        title = request.POST.get('title')
        whatsapp = request.POST.get('whatsapp')

        personaldata = PersonalData.objects.get(id=id)

        personaldata = PersonalData(
            id=id, name=name, profession=profession,
            title=title, whatsapp=whatsapp)
        personaldata.save()
        return redirect(reverse('portifolio:home'))


def createsocialmedia(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


def editsocialmedia(request):
    if request.method == 'POST':
        id = request.POST.get('minicard_id')
        name = request.POST.get('name')
        icon = request.POST.get('icon')
        link = request.POST.get('link')

        socialmedia = MiniCard.objects.get(id=id)

        socialmedia = MiniCard(
            id=id, name=name, icon=icon, link=link)
        socialmedia.save()
        return redirect(reverse('portifolio:home'))


def deleteminicard(request, minicard_id):
    if not request.POST:
        raise Http404()

    minicard = MiniCard.objects.get(id=minicard_id)

    if not minicard:
        raise Http404()
    minicard.delete()

    return redirect(reverse('portifolio:home'))


def createabout(request):
    form = AboutForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


def editabout(request):
    if request.method == 'POST':
        id = request.POST.get('about_id')
        title = request.POST.get('title')
        about_me = request.POST.get('aboutme')

        aboutmedata = About.objects.get(id=id)

        aboutmedata = About(
            id=id, title=title, aboutme=about_me)
        aboutmedata.save()
        return redirect(reverse('portifolio:home'))


def createbarprogress(request):
    form = BarProgressForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


def editbarprogress(request):
    if request.method == 'POST':
        id = request.POST.get('barprogress_id')
        title = request.POST.get('title')
        progress = request.POST.get('progress')

        barprogress = BarProgress.objects.get(id=id)

        barprogress = BarProgress(
            id=id, title=title, progress=progress)
        barprogress.save()
        return redirect(reverse('portifolio:home'))


def deletebarprogress(request, barprogress_id):
    if not request.POST:
        raise Http404()

    barprogress = BarProgress.objects.get(id=barprogress_id)

    if not barprogress:
        raise Http404()
    barprogress.delete()

    return redirect(reverse('portifolio:home'))


def createskills(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        skill = form.save(commit=False)
        skill.skills = True
        skill.save()
        return redirect(reverse('portifolio:home'))


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


def createcards(request):
    form = CardForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))


def editcard(request):
    if request.method == 'POST':
        id = request.POST.get('card_id')
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        icon = request.POST.get('icon')
        linkgithub = request.POST.get('linkgithub')
        linkdeploy = request.POST.get('linkdeploy')
        datainfo = request.POST.get('datainfo')
        section = request.POST.get('section')

        card = Card.objects.get(id=id)
        card = Card(id=id, title=title, subtitle=subtitle, icon=icon,
                    linkgithub=linkgithub, linkdeploy=linkdeploy,
                    datainfo=datainfo, section=section)
        card.save()
        return redirect(reverse('portifolio:home'))
