from django.shortcuts import render
from django.views import generic
from .models import Topic

# Create your views here.
class TopicList(generic.ListView):
    queryset = Topic.objects.filter(status=1).order_by('-created_on')
    template_name = 'topics.html'

class TopicDetail(generic.DetailView):
    model = Topic
    template_name = 'topic_detail.html'