from django.db import models

from image_cropping import ImageRatioField, ImageCropField
from tinymce.models import HTMLField


# Create your models here.


class Galleria(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    didascalia = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image', '500x480')
    slider = ImageRatioField('image', '870x480')
    thumb = ImageRatioField('image', '132x94')
    croppinguno = ImageRatioField('image', '1140x487')
    croppingdue = ImageRatioField('image', '198x132')
    croppingtre = ImageRatioField('image', '1199x674')
    croppingquattro = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
    croppingcinque = ImageRatioField('image', '1200x800', verbose_name="Design HD")
    croppingsei = ImageRatioField('image', '1200x1125', verbose_name="News")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

class Slider(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    titolo_uk = models.CharField(max_length=100, verbose_name="Titolo Inglese:")
    link = models.CharField(max_length=100, verbose_name="Link")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    body = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image', '1170x500')
    slider = ImageRatioField('image', '870x480')
    thumb = ImageRatioField('image', '132x94')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

class Post(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    intro = models.TextField(null=True, blank=True, verbose_name="Intro")
    intro_uk = models.TextField(null=True, blank=True, verbose_name="Intro Inglese")
    body = HTMLField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = HTMLField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    miniatura = ImageRatioField('image', '500x281')
    cropping = ImageRatioField('image', '1200x675')
    galleria = models.ManyToManyField(Galleria, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Post"

class Page(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    intro = models.TextField(null=True, blank=True, verbose_name="Intro")
    intro_uk = models.TextField(null=True, blank=True, verbose_name="Intro Inglese")
    body = HTMLField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = HTMLField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    miniatura = ImageRatioField('image', '300x200')
    cropping = ImageRatioField('image', '1200x675')
    galleria = models.ManyToManyField(Galleria, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Progetti"

class News(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    intro = models.TextField(null=True, blank=True, verbose_name="Intro")
    intro_uk = models.TextField(null=True, blank=True, verbose_name="Intro Inglese")
    body = HTMLField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = HTMLField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    miniatura = ImageRatioField('image', '500x281')
    cropping = ImageRatioField('image', '1200x675')
    galleria = models.ManyToManyField(Galleria, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "News"

class Link(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_uk = models.CharField("Titolo Inglese:", max_length=100, null=True, blank=True)
    email = models.CharField("Email:", max_length=100, null=True, blank=True)
    url = models.CharField("Link:", max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    miniatura = ImageRatioField('image', '500x281')
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Link"
