from django.urls import path
from . import views
from django.http import JsonResponse

#def process_command(request):
 #   return JsonResponse({"message": "Processing command..."})

urlpatterns = [
    path('', views.home, name='home'),  # For rendering the HTML page
   # path('process_command/', views.process_command, name='process_command'), 
     path('ask/', views.ask, name='ask'), # For processing voice commands
]
