from django.shortcuts import render, get_object_or_404
from .models import Topic

# Create your views here.
def home(request):
    topics = Topic.objects.all()
    return render(request, 'jobs/home.html', {'topics': topics})

def detail(request, topic_id):
    topic_detail = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'jobs/detail.html', {'topic':topic_detail})

def contact(request):
    return render(request, 'jobs/contact.html')

def about(request):
    return render(request, 'jobs/about.html')

def counselling(request):
    return render(request, 'jobs/counselling.html')
