from django.shortcuts import render

# Create your views here


# kblogs/views.py

from django.http import HttpResponse
from datetime import datetime

def katesfun(request):
    #return HttpResponse("Poupou cate said hi to you :)")
    return render(request, 'show_poupou.html', {
        'current_time': str(datetime.now()),
    })
