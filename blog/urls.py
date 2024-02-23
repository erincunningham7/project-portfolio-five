from . import views
from django.urls import path

urlpatterns = [
    path('', views.Topic.as_view(), name='topics'),
    path('<slug:slug>/', views.TopicDetail.as_view(), name='topic_detail'),
]