from django.contrib import admin

from .models import About, BarProgress, Card, MiniCard, PersonalData


# Register your models here.
class BarProgressInlines(admin.TabularInline):
    model = BarProgress
    extra = 1


class CardInlines(admin.TabularInline):
    model = Card
    extra = 1


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']

    inlines = [
        BarProgressInlines,
        CardInlines,
    ]


admin.site.register(PersonalData, PersonalDataAdmin)


class MiniCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skills']


admin.site.register(MiniCard, MiniCardAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'aboutme']


admin.site.register(About, AboutAdmin)
