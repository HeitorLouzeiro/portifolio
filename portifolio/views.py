from django.shortcuts import render

from portifolio.models import PersonalData, SocialMedia


# Create your views here.
def home(request):
    template_name = 'portifolio/pages/home.html'
    personaldatas = PersonalData.objects.all()[:1]
    socialmedias = SocialMedia.objects.all()
    context = {
        'personaldatas': personaldatas,
        'socialmedias': socialmedias,
    }
    return render(request, template_name, context)
