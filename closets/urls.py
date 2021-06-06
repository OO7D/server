from django.urls import path
from . import views

urlpatterns = [
    path('api/closet/', views.ClosetListCreate.as_view() ),
]