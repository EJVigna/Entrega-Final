from django.urls import path
from Final import views

app_name = 'Final'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    
]