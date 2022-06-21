from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def home(request):
  data = Article.objects.all().order_by('date')
  params = {
    'data':data
  }

  return render (request, 'index.html', params)

def details (request, id):
  full_detail = Article.objects.get(id = id)
  param = {
    'data' : full_detail
  }
  return render(request, 'detail.html', param)

@login_required(login_url='/second/login/')
def create_art(request):
  if request.method == 'POST':
    form = forms.CreateArticle(request.POST, request.FILES)
    if form.is_valid():
    # add to db
      firstOfAll = form.save(commit=False)
      firstOfAll.author = request.user 
    #this line comes after the foreign key has been called in the model. it assigns the current logged-in user from the request to 'author' field.
      firstOfAll.save()
      return redirect('main1:home')
  else:
    form = forms.CreateArticle()
  params = {
    'data' : form
  }
  return render(request, 'create.html', params)

@login_required(login_url='/second/login/')
def update_art(request, id):
  collect = Article.objects.get(id=id)
  if request.method == 'POST':
    form = forms.CreateArticle(request.POST, request.FILES, instance=collect) # prepopulate the form
    if form.is_valid():
    # add to db
      firstOfAll = form.save(commit=False)
      firstOfAll.author = request.user
      firstOfAll.save()
      return redirect('main1:detail', id)
  else:
    form = forms.CreateArticle(instance=collect)
  params = {
    'data' : form
  }
  return render(request, 'update.html', params)

@login_required(login_url='/second/login/')
def delete_art(request, id):
  title_display = Article.objects.get(id=id) #we need this for both GET and POST
  if request.method == 'POST':
    title_display.delete() #delete record from database
    return redirect('main1:home')
  params ={
    'data':title_display
  }
  return render(request, 'delete.html', params)