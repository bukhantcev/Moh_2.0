from django.shortcuts import render

# Create your views here.
def index(request):#--------------------------------------------ROOM
    return render(request, 'room/index.html')