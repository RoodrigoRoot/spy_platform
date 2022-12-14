from django.urls import path

from src.hitmens.views import HitmenListView, HitmenDetailsDetailView

app_name ='hitmens'

urlpatterns = [

    path('hitmen/', HitmenListView.as_view(), name="hitmens"),
    path('hitmen/<int:pk>/', HitmenDetailsDetailView.as_view(), name="hitmen_details"),

]

