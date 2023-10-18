from django.shortcuts import render
from .models import Name

# Create your views here.
def site(request):
    return render(request, 'site.html')