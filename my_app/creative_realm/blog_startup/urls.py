from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('poetry',views.poetry, name='poetry'),
    path('musings',views.musings, name='musings'),
    path('fiction',views.fiction, name='fiction'),
    path('misc',views.misc, name='misc'),
    path('sayhi',views.sayhi, name='sayhi'),
]
