from django.shortcuts import render, get_list_or_404, get_object_or_404

# blog app
from blog.models import Post

from user_auth.models import Profile


def home(request):
    """Returns all posts"""
    all_posts = Post.objects.all()

    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = ''

    context = {'all_posts': all_posts, 'profile': profile}
    # context = {'all_posts': all_posts[0:8], 'profile': profile}
    template = 'home.html'

    return render(request, template, context)

