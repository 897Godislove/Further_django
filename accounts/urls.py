from django.urls import path
from . import views as v

app_name = 'accounts'
urlpatterns = [
  path('signup/', v.signup_auth, name='signup'),
  path('login/', v.login_auth, name='login'),
  path('logout/', v.logout_auth, name='logout')
]

