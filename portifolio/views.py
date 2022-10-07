from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import PersonalDataForm
from .models import About, BarProgress, Card, PersonalData, SocialMedia


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    socialmedias = SocialMedia.objects.all()
    about = About.objects.all()[:1]
    barprogress = BarProgress.objects.all()
    cards = Card.objects.all()

    form = PersonalDataForm
    context = {
        'personaldatas': personaldatas,
        'socialmedias': socialmedias,
        'about': about,
        'barprogress': barprogress,
        'cards': cards,

        'form': form,
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
