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

def details (request, pk):
  return HttpResponse(pk)