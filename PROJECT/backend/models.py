from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
)
    website=models.URLField()
    bio=models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=50,blank=False)
    subtitle=models.CharField(max_length=100,blank=False)
    body=models.TextField()
    slug=models.SlugField(max_length=255, unique=True)
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)










