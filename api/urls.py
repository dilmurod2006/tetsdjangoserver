from django.urls import path
from .views import PostList, Detailpost

urlpatterns = [
    path('<int:pk>/', Detailpost.as_view()),
    path('',PostList.as_view()),
]
