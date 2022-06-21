from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  
  date = models.DateTimeField(auto_now_add = True)
  thumb = models.ImageField(default='default.jpg', blank=True, upload_to='upload/')
  
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.title

  def snippet(self):
    # if self.body >= [50]:
    #   cut = self.body[:50] + '...'
    # else:
    #   cut = self.body
    # return cut
    return self.body[:50] + '...'

  