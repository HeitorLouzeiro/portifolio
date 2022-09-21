from django.db import models

# Create your models here.


class PersonalData(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    whatsapp = models.CharField(max_length=50)


class SocialMedia(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    personaldata = models.ForeignKey(PersonalData, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
