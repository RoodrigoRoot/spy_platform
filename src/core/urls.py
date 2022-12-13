from django.urls import path

from src.core.views import LoginView, logout_view, Indexview, RegisterHitmenView
app_name ='core'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterHitmenView.as_view(), name='register'),
    path('', Indexview.as_view(), name='home'),
]
