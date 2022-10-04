from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('delete', views.delete, name='delete'),
    path('reservation/', views.choose, name='choose'),
    path('reservation/id-<id>', views.reservation, name='reservation'),
]
