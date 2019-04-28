from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('events/', views.get_events, name='events'),
    path('allEvents/', views.get_all_event, name='all_events'),
    path('locations/', views.get_locations, name='locations'),
    path('casas/', views.get_casas, name='casas')
]
