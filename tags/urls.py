from django.urls import path
from tags import views

urlpatterns = [
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view()),
]
