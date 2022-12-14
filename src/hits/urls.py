from django.urls import path

from src.hits.views import HitsView, HitDetailView, HitCreateView

app_name ='hits'

urlpatterns = [
    path('hits/', HitsView.as_view(), name='hits'),
    path('hits/<int:pk>/', HitDetailView.as_view(), name='details_hit'),
    path('hits/create/', HitCreateView.as_view(), name='create_hit'),
]
