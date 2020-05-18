from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('movie/', views.movie, name="movie"),
    path('drama/', views.drama, name="drama"),
    path('entertain/', views.entertain, name="entertain"),
    path('<int:article_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
]