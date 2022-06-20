from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.song_list),
    # path('<int:pk>/', views.song_list())
    ]