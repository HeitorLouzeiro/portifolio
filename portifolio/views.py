from django.shortcuts import render

from portifolio.models import About, PersonalData, SocialMedia


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    socialmedias = SocialMedia.objects.all()
    about = About.objects.all()[:1]
    context = {
        'personaldatas': personaldatas,
        'socialmedias': socialmedias,
        'about': about,
    }
    return render(request, template_name, context)
