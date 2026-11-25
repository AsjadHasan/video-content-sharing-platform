from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Tagtitle

class HomeView(View):
    def get(self, request):
        tag_names = Tagtitle.objects.all().values_list('title', flat=True)
        return render(request, 'home.html', {'top_button_names': tag_names})