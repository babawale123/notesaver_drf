from django.urls import path
from .views import SignUp,Login,Test

urlpatterns = [
   path('',SignUp), 
   path('login/',Login),    
   path('test/', Test.as_view())
]
