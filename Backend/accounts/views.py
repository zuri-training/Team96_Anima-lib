from django.shortcuts import render
from .models import Lib
from django.core.paginator import Paginator


# Create your views here.


# Landing page view
def index(request):
    animation_objects = Lib.objects.all()
    paginator = Paginator(animation_objects,8)
    page = request.GET.get('page') 
    animation_objects = paginator.get_page(page)   
    return render(request, 'accounts/index.html', {'animation_objects': animation_objects}) 
