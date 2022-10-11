from django.db import models

# Create your models here.


class PersonalData(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    whatsapp = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(
        upload_to='portifolio/user/cover/%Y/%m/%d/', blank=True)
    pdf = models.FileField(
        upload_to='portifolio/user/pdf/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name+" "+self.profession


class MiniCard(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    skills = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BarProgress(models.Model):
    title = models.CharField(max_length=50)
    progress = models.CharField(max_length=3)

    def __str__(self):
        return self.title+" "+self.progress


class About(models.Model):
    title = models.CharField(max_length=50)
    aboutme = models.TextField()

    def __str__(self):
        return self.title


class Card(models.Model):
    SECTION = (
        ('1', 'About'),
        ('2', 'Curriculum'),
        ('3', 'Services'),
        ('4', 'Portfolio'),
    )
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100, blank=True)
    linkgithub = models.CharField(max_length=100, blank=True)
    linkdeploy = models.CharField(max_length=100, blank=True)
    datainfo = models.CharField(max_length=30, blank=True)
    section = models.CharField(max_length=1, choices=SECTION)
    cover = models.ImageField(
        upload_to='portifolio/projects/cover/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title+" "+self.section
