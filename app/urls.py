from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home_page'),
    path('downloadCV/',views.CV,name='cv'),
    path('contact/',views.contact_form_view,name='contact_form'),
]