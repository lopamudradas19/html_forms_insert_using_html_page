from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')



    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        topic = request.POST['tn']
        TO=Topic.objects.get(topic_name=topic)
        name=request.POST['name']
        url=request.POST['url']
        WO=webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('Insertion of webpage is Done')



    return render(request,'insert_webpage.html')


def insert_accessrecord(request):
    if request.method=='POST':
        name=request.POST['name']
        WO=webpage.objects.get(name=name)
        date=request.POST['date']
        author=request.POST['author']
        AO=accessrecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('Insertion of accessrecord is Done')



    return render(request,'insert_accessrecord.html')