from . import views
from django.urls import path

app_name = 'main1'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create_art, name='create'),
    path('update/<int:id>', views.update_art, name='update'),
    path('detail/<int:id>', views.details, name='detail'),
    path('delete/<int:id>', views.delete_art, name='delete')
]


