from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import MiniCardForm, PersonalDataForm
from .models import About, BarProgress, Card, MiniCard, PersonalData


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    minicards = MiniCard.objects.all()
    about = About.objects.all()[:1]
    barprogress = BarProgress.objects.all()
    cards = Card.objects.all()

    form = PersonalDataForm
    form_minicard = MiniCardForm
    context = {
        'personaldatas': personaldatas,
        'minicards': minicards,
        'about': about,
        'barprogress': barprogress,
        'cards': cards,

        'form': form,
        'form_minicard': form_minicard,
    }
    return render(request, template_name, context)


def createpersonaldata(request):
    form = PersonalDataForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))

    context = {
        'form': form,
    }
    return render(request, context)


def editpersonaldata(request):
    if request.method == 'POST':
        id = request.POST.get('personaldata_id')
        name = request.POST.get('name')
        profession = request.POST.get('profession')
        title = request.POST.get('title')
        whatsapp = request.POST.get('whatsapp')

        personaldata = PersonalData.objects.get(id=id)

        personaldata = PersonalData(
            id=id, name=name, profession=profession, title=title, whatsapp=whatsapp)
        personaldata.save()
        return redirect(reverse('portifolio:home'))


def createsocialmedia(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse('portifolio:home'))

    context = {
        'form': form,
    }
    return render(request, context)


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

    return HttpResponse('Mini Card Apagado com sucesso!')
