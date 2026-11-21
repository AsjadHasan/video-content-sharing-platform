from django.shortcuts import render

# Create your views here.
from django.views import View

class HomeView(View):
    def get(self, request):
        tag_names = [
            'All', 'Music', 'Mixes', 'Technology', 'Programming', 
            'Live', 'Gaming', 'Podcasts', 'Travel', 'Education', 
            'Recently uploaded', 'Watched', 'Sports', 'News', 'Comedy', 'Movies', 'Fashion',
            'Science', 'Health', 'Business', 'Finance', 'Food', 'Art', 'Photography', 'DIY', 'Animation', 'Documentary',
            'History', 'Nature', 'Animals', 'Cars', 'Motorcycles', 'Space', 'Weather', 'Politics', 'Culture', 
            'Religion', 'Philosophy', 'Psychology', 'Self-help', 'Motivation', 
            'Inspiration', 'Fitness', 'Yoga', 'Meditation', 'Mindfulness', 
            'Parenting', 'Relationships', 'Dating', 'Love', 'Friendship', 
            'Social Media', 'Marketing', 'Advertising', 'Entrepreneurship', 
            'Startups', 'Investing', 'Real Estate', 'Economics'
        ]
        return render(request, 'home.html', {'top_button_names': tag_names})