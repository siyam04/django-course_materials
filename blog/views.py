from django.shortcuts import (

    render,
    get_object_or_404,
    get_list_or_404,

)


# App importing
from blog.models import Post


def post_list(request):
    """Returns all posts"""
    all_posts = get_list_or_404(Post)
    # all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    template = 'blog/post_list.html'
    return render(request, template, context)


def post_detail(request, id=None):
    """Returns single post"""
    single_post = get_object_or_404(Post, id=id)
    # single_post = Post.objects.get(id=id)
    context = {'single_post': single_post}
    template = 'blog/single_post.html'
    return render(request, template, context)

