from django.contrib import admin

from .models import PersonalData, SocialMedia

# Register your models here.


class SocialMediaInlines(admin.TabularInline):
    model = SocialMedia
    extra = 1


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession']

    inlines = [
        SocialMediaInlines
    ]


admin.site.register(PersonalData, PersonalDataAdmin)
