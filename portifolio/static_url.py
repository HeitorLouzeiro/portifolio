from django.shortcuts import redirect
from django.urls import reverse


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
    elif cardaction is False:
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
    else:
        if card.section == '1':

            return url_about()
        elif card.section == '2':

            return url_curriculum()
        elif card.section == '3':

            return url_services()
        elif card.section == '4':

            return url_portfolio()
        else:
            return redirect(reverse('portifolio:home'))
