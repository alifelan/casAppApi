from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('events/', views.get_events, name='events'),
    path('allEvents/', views.get_all_events, name='all_events'),
    path('locations/', views.get_locations, name='locations'),
    path('casas/', views.get_casas, name='casas'),
    path('student/<str:mat>/', views.student_detail, name='student_detail'),
    path('addEvent/', views.add_event, name='add_event'),
    path('removeEvent/', views.remove_event, name='remove_event'),
    path('addClass/', views.add_class, name='add_class'),
]
