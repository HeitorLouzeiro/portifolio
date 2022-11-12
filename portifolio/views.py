import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render

from .forms import (AboutForm, BarProgressForm, CardForm, MiniCardForm,
                    PersonalDataForm)
from .models import About, BarProgress, Card, MiniCard, PersonalData
from .static_url import (redirect_action_card, url_about, url_contact,
                         url_curriculum, url_home)


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
        messages.success(request, 'Data saved successfully!')
        return url_home()
    messages.error(request, 'Failed to save data!')
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editpersonaldata(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('personaldata_id')
    personaldata = get_object_or_404(PersonalData, id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(personaldata.cover) > 0:
                os.remove(personaldata.cover.path)
            personaldata.cover = request.FILES['cover']
    personaldata.name = request.POST.get('name')
    personaldata.profession = request.POST.get('profession')
    personaldata.title = request.POST.get('title')
    personaldata.whatsapp = request.POST.get('whatsapp')

    if not personaldata.name or not personaldata.profession \
            or not personaldata.title:
        messages.error(request, 'Fields with (*) cannot be empty!')
        return url_home()

    personaldata.save()
    messages.success(request, 'Data saved successfully.')
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createsocialmedia(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Data saved successfully!')
        return url_home()

    messages.error(request, 'Failed to save data!')
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editsocialmedia(request):
    if not request.POST:
        raise Http404()
    id = request.POST.get('minicard_id')
    socialmedia = get_object_or_404(MiniCard, id=id)
    if request.method == 'POST':
        socialmedia.name = request.POST.get('name')
        socialmedia.icon = request.POST.get('icon')
        socialmedia.link = request.POST.get('link')
    if not socialmedia.name or not socialmedia.icon:
        messages.error(request, 'Fields with (*) cannot be empty!')
        return url_home()

    socialmedia.save()
    messages.success(request, 'Data saved successfully!')
    return url_home()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deleteminicard(request, minicard_id):
    if not request.POST:
        raise Http404()
    minicard = get_object_or_404(MiniCard, id=minicard_id)

    if minicard.skills is False:
        minicard.delete()
        messages.success(request, 'Social Media successfully deleted!')
        return url_home()
    else:
        minicard.delete()
        messages.success(request, 'Skill Deleted successfully!')
        return url_curriculum()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createabout(request):
    form = AboutForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Data saved successfully!')
        return url_about()
    messages.error(request, 'Failed to Save Data!')
    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editabout(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('about_id')
    aboutmedata = get_object_or_404(About, id=id)

    if request.method == 'POST':
        aboutmedata.title = request.POST.get('title')
        aboutmedata.aboutme = request.POST.get('aboutme')

    if not aboutmedata.title or aboutmedata.aboutme:
        aboutmedata.save()
        messages.success(request, 'Data saved successfully!')
        return url_about()

    messages.error(request, 'Fields with (*) cannot be empty!')
    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createbarprogress(request):
    form = BarProgressForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Data saved successfully!')
        return url_about()
    messages.error(request, 'Failed to Save Data!')
    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editbarprogress(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('barprogress_id')

    barprogress = get_object_or_404(BarProgress, id=id)

    if request.method == 'POST':
        barprogress.title = request.POST.get('title')
        barprogress.progress = request.POST.get('progress')
    if not barprogress.title or barprogress.progress:
        messages.error(request, 'Fields with (*) cannot be empty!')

    barprogress.save()
    messages.success(request, 'Data saved successfully!')
    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletebarprogress(request, barprogress_id):
    if not request.POST:
        raise Http404()

    barprogress = get_object_or_404(BarProgress, id=barprogress_id)

    barprogress.delete()
    messages.success(request, 'Data successfully deleted!')
    return url_about()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createskills(request):
    form = MiniCardForm(request.POST or None)

    if form.is_valid():
        skill = form.save(commit=False)
        skill.skills = True
        skill.save()
        messages.success(request, 'Data saved successfully!')
        return url_curriculum()
    messages.error(request, 'Failed to Save Data!')
    return url_curriculum()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editskills(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('minicard_id')
    skills = get_object_or_404(MiniCard, id=id)

    if request.method == 'POST':
        skills.name = request.POST.get('name')
        skills.icon = request.POST.get('icon')
        skills.link = request.POST.get('link')
        skills.skills = True

    if not skills.name or skills.icon:
        messages.error(request, 'Fields with (*) cannot be empty!')

    skills.save()
    messages.success(request, 'Data saved successfully!')
    return url_curriculum()


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def createcards(request):
    form = CardForm(request.POST, request.FILES or None)

    if form.is_valid():
        card = form.save(commit=False)
        cardaction = True
        messages.success(request, 'Data saved successfully!')
        return redirect_action_card(card, cardaction)

    messages.error(request, 'Failed to Save Data!')
    return redirect_action_card(card, cardaction)


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def editcard(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('card_id')
    card = get_object_or_404(Card, id=id)

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
        if not card.title:
            messages.error(request, 'Fields with (*) cannot be empty!')
        return redirect_action_card(card, cardaction)
    messages.success(request, 'Data saved successfully!')
    return redirect_action_card(card, cardaction)


@login_required(login_url='accounts:loginUser', redirect_field_name='next')
def deletecard(request):
    if not request.POST:
        raise Http404()

    id = request.POST.get('card_id')
    card = get_object_or_404(Card, id=id)

    cardaction = False
    messages.success(request, 'Data successfully deleted!')
    return redirect_action_card(card, cardaction)


def sendemail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if not name:
            messages.error(request, 'Fields with (*) cannot be empty!')
            return url_contact()
        if not email:
            messages.error(request, 'Fields with (*) cannot be empty!')
            return url_contact()
        if not subject:
            messages.error(request, 'Fields with (*) cannot be empty!')
            return url_contact()
        if not message:
            messages.error(request, 'Fields with (*) cannot be empty!')
            return url_contact()

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        message = '''
        Name:{}
        New message: {}
        From: {}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['subject'], message, '', [
                  os.environ.get('EMAIL_HOST_USER')])
        messages.success(request, 'E-mail successfully sent!')
        return url_contact()
