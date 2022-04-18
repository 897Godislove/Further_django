from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
  data = Article.objects.all().order_by('date')
  params = {
    'data':data
  }

  return render (request, 'index.html', params)

def details (request, slug):
  full_detail = Article.objects.get(slug = slug)
  param = {
    'data' : full_detail
  }
  return render(request, 'detail.html', param)