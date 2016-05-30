from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150,unique=True)
    def __unicode__(self):
        return self.name


def get_default_category():
    return Category.objects.get_or_create(name="Uncategorized")

class Articles(models.Model):
    title = models.CharField(max_length=200)
    category=models.ForeignKey("Category", default=get_default_category)
    summary = models.TextField(null=True,blank=True)
    author= models.ForeignKey(User)
    hero_image=models.ImageField(upload_to ='media/',null=True,blank=False)
    extra_image=models.ImageField(upload_to ='media/',null=True,blank=True)
    publication_date= models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title