from django.contrib import admin

from .models import About, BarProgress, Card, MiniCard, PersonalData


# Register your models here.
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']

admin.site.register(PersonalData, PersonalDataAdmin)


class MiniCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skills']


admin.site.register(MiniCard, MiniCardAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'aboutme']


admin.site.register(About, AboutAdmin)


class BarProgressAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'progress']


admin.site.register(BarProgress, BarProgressAdmin)

class CardsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'section']


admin.site.register(Card, CardsAdmin)
