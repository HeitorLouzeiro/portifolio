from django.contrib import admin

from .models import About, Card, PersonalData, SocialMedia

# Register your models here.


class SocialMediaInlines(admin.TabularInline):
    model = SocialMedia
    extra = 1


class AboutInlines(admin.TabularInline):
    model = About
    extra = 1


class CardInlines(admin.TabularInline):
    model = Card
    extra = 1


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']

    inlines = [
        SocialMediaInlines,
        AboutInlines,
        CardInlines,
    ]


admin.site.register(PersonalData, PersonalDataAdmin)
