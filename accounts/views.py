from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.

# signup function
def signup_auth(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # log the user in
      user = form.save()
      # login(request, user)
      messages.success(request, "You have successfully signed up to this site. Welcome!")
      return redirect('main1:home')
  else:
      form = UserCreationForm() 

  params = {
    'data' : form
  }
  # params['data'] = nfkr
  return render(request, 'signup.html', params)

# login function
def login_auth(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST) 
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      if 'after' in request.POST:
        return redirect(request.POST.get('after'))
      else:
        messages.success(request, "You are logged in succesfully")
        return redirect('main1:home')
  else:
    form = AuthenticationForm()
  param = {
    'data' : form
  }
  return render(request, 'login.html', param)

# logout function
def logout_auth(request):
  if request.method == 'POST':
    logout(request)
    return redirect('main1:home')