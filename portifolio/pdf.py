from django.shortcuts import render

from .models import About, BarProgress, Card, MiniCard, PersonalData


def pdf(request):
    template_name = 'portifolio/pages/pdf.html'
    personaldatas = PersonalData.objects.all()[:1]
    minicards = MiniCard.objects.all()
    about = About.objects.all()[:1]
    barprogress = BarProgress.objects.all()
    cards = Card.objects.all()

    context = {
        'personaldatas': personaldatas,
        'minicards': minicards,
        'about': about,
        'barprogress': barprogress,
        'cards': cards,
    }
    return render(request, template_name, context)
