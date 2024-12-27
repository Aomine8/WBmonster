from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReadCards.as_view(), name='cards'),
    path('<int:pk>', views.DetailCard.as_view(), name='card'),
]