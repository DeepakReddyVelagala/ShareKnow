from django.shortcuts import render, redirect
from core.models import Topic, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    getTopic(request)
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def topic(request, topic):
    username = request.GET.get('username')
    topic_details = Topic.objects.get(name=topic)
    return render(request, 'topic_messages.html', {
        'username': username,
        'topic': topic,
        'topic_details': topic_details
    })

def checkview(request):
    topic = request.POST['topic']
    username = request.POST['username']

    if Topic.objects.filter(name=topic).exists():
        return redirect('/'+topic+'/?username='+username)
    else:
        new_topic = Topic.objects.create(name=topic)
        new_topic.save()
        return redirect('/'+topic+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    topic_id = request.POST['topic_id']

    new_message = Message.objects.create(value=message, user=username, topic=topic_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, topic):
    topic_details = Topic.objects.get(name=topic)

    messages = Message.objects.filter(topic=topic_details.id)
    return JsonResponse({"messages":list(messages.values())})


def getTopic(request):

    topics = Topic.objects
    
    return JsonResponse({"topics":list(topics.values())})