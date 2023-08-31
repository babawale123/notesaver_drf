from django.urls import path
from .views import AddAndGetNote,DetailsView
urlpatterns = [
    
    path('',AddAndGetNote.as_view()),
    path('details/<int:pk>/',DetailsView.as_view())

    ]
