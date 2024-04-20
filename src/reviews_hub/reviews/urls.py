from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:review_id>/', views.like_review, name='like_review'),
]
