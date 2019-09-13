from django.shortcuts import render

posts = [
    {
        'author': 'Yun Kim',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 12, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 13, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
