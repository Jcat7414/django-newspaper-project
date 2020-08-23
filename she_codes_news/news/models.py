from django.db import models
from django.utils import timezone
from django.forms import ModelForm



class Family(models.Model):
    FOUNDER = "Founder" 
    PARTNER = "Partner"
    MENTOR = "Mentor"
    TEAM = "Team"
    ADVOCATE = "Advocate"
    FAMILY_TYPE = [
        (FOUNDER, "Founder"), 
        (PARTNER, "Partner"), 
        (MENTOR, "Mentor"),
        (TEAM, "Flair Team"), 
        (ADVOCATE, "Advocate")
    ]
    type = models.CharField(max_length=20, choices=FAMILY_TYPE, default=FOUNDER)

    def get_queryset(self):
            '''Return all family types.'''
            return self.type()

    # def __str__(self):
    #     return self.type

class NewsStory(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True, story_name="Created at")
    # updated_at = models.DateTimeField(auto_now=True, story_name="Updated at")
    title = models.CharField(max_length=200, verbose_name="story title")
    author = models.CharField(max_length=200, verbose_name="written by")
    pub_date = models.DateTimeField(verbose_name="date published")
    category = models.CharField(max_length=20, verbose_name="story category", default='Type of Story')
    content = models.TextField(verbose_name="")
    linkedin_url = models.CharField(max_length=200, verbose_name="linkedIn profile URL", default="Paste your LinkedIn URL here")
    image = models.ImageField(upload_to='story/images', verbose_name="story photo", default="placeholder-1.jpg")
    @property
    def better_date(self):
        if self.pub_date:
            return self.pub_date.strftime("%d %b %Y")
        else:
            return "no_date"
    # @formname
    # def get_verbose_name(object):
    #     return object._meta.verbose_name

# class Image(models.Model):
#     title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')

