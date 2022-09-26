from django.shortcuts import render

from portifolio.models import (About, BarProgress, Card, PersonalData,
                               SocialMedia)


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    socialmedias = SocialMedia.objects.all()
    about = About.objects.all()[:1]
    barprogress = BarProgress.objects.all()
    cards = Card.objects.all()

    context = {
        'personaldatas': personaldatas,
        'socialmedias': socialmedias,
        'about': about,
        'barprogress': barprogress,
        'cards': cards,
    }
    return render(request, template_name, context)
