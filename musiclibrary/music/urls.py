from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    ]