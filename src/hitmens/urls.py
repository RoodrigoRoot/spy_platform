from django.urls import path

from src.hitmens.views import HitmenListView

app_name ='hitmens'

urlpatterns = [
    path('hitmens/', HitmenListView.as_view(), name="hitmens"),
]

