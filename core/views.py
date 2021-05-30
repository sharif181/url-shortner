from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def create(request):
    print(request)
    if request.method == "POST":
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(url=url,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def visit(request,pk):
    urlInfo = Url.objects.get(uuid=pk)
    return redirect("https://"+urlInfo.url)