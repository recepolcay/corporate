from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=100,verbose_name=_("Ad Soyad"))
    phone=models.CharField(max_length=15,verbose_name=_("Telefon"))
    email=models.EmailField()
    message=models.TextField(verbose_name=_("Mesaj"))


class About(models.Model):
    title=models.CharField(max_length=100)
    content=RichTextField()

class Service(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("Başlık"))
    content=RichTextField(verbose_name=_("İçerik"))
    slug=models.SlugField(max_length=200,blank=True,editable=False)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Service,self).save(*args,**kwargs)


class Slider(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='slider')


class Category(models.Model):
    name=models.CharField(max_length=200,verbose_name=_("Ad"))
    slug=models.SlugField(max_length=100,unique=True,blank=True,editable=False)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

        

class Blog(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("Başlık"))
    image=models.ImageField(upload_to='blogs')
    content=RichTextField(verbose_name=_("İçerik"))
    category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=_("Kategori"))
    views=models.IntegerField(default=0,verbose_name=_("Görüntülenme"))
    slug=models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name=_("Oluşturulma Tarihi"))
    updated_at=models.DateTimeField(auto_now=True,verbose_name=_("Güncellenme Tarihi"))
    tags=TaggableManager()

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Setting(models.Model):
    logo_1=models.ImageField(upload_to='dimg',null=True,blank=True,verbose_name=_("Logo 1"))
    logo_2=models.ImageField(upload_to='dimg',null=True,blank=True,verbose_name=_("logo 2"))
    title=models.CharField(max_length=255,verbose_name=_("Başlık"))
    description=models.CharField(max_length=255,verbose_name=_("Açıklama"))
    keywords=models.CharField(max_length=255,verbose_name=_("Anahtar Kelimeler"))
    phone_fixed=models.CharField(max_length=15,verbose_name=_("Sabit Telefon"))
    phone_mobile=models.CharField(max_length=15,verbose_name=_("Cep Telefonu"))
    fax=models.CharField(max_length=15,verbose_name=_("Faks"))
    email=models.EmailField()
    city=models.CharField(max_length=50,verbose_name=_("Şehir"))
    district=models.CharField(max_length=50,verbose_name=_("İlçe"))
    address=models.TextField(verbose_name=_("Adres"))
    postal_code=models.CharField(max_length=10,verbose_name=_("Posta Kodu"))
    facebook_url=models.URLField(max_length=255,verbose_name=_("Facebook"))
    twitter_url=models.URLField(max_length=255,verbose_name=_("Twitter - X"))
    instagram_url=models.URLField(max_length=255,verbose_name=_("Instagram"))
    youtube_url=models.URLField(max_length=255,verbose_name=_("Youtube"))

class Page(models.Model):
    title=models.CharField(max_length=200,verbose_name=_('Başlık'))
    content=RichTextField(verbose_name=_('İçerik'))
    slug=models.SlugField(max_length=200,blank=True,editable=False)

    def get_absolute_url(self):
        return reverse('page-detail',kwargs={'slug':self.slug})


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Page,self).save(*args,**kwargs)
