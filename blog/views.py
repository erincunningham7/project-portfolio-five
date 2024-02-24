from django.shortcuts import render
from django.views import generic
from .models import Topic


# Create your views here.
class TopicList(generic.ListView):
    """
    A view to render a list of blog topics
    """
    queryset = Topic.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/topics.html"


class TopicDetail(generic.DetailView):
    """
    A view to provide a detail view of the full blog entry
    """
    model = Topic
    template_name = "blog/topic_detail.html"
