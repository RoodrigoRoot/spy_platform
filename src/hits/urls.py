from django.urls import path

from src.hits.views import HitsView, HitDetailView

app_name ='hits'

urlpatterns = [
    path('hits/', HitsView.as_view(), name='hits'),
    path('hits/<int:pk>/', HitDetailView.as_view(), name='details_hit'),
]
