from django.shortcuts import (

    render,
    get_object_or_404,
    get_list_or_404,
    redirect,
)

# App importing
from blog.models import Post
from blog.forms import PostCreateForm


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
    template = 'blog/post_detail.html'
    return render(request, template, context)


def post_create(request):
    """Creating single post"""
    if request.method == 'POST':
        create_form = PostCreateForm(request.POST)
        if create_form.is_valid():
            # post_created = create_form.save(commit=False)
            create_form.save()
            return redirect('list')

    create_form = PostCreateForm()

    context = {'create_form': create_form}
    template = 'blog/post_crate.html'

    return render(request, template, context)


def post_update(request, id=None):
    """Update a post"""
    post_query = Post.objects.get(id=id)
    update_form = PostCreateForm(request.POST or None, instance=post_query)

    if request.method == 'POST':
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', id=post_query.id)

    context = {'update_form': update_form}
    template = 'blog/post_update.html'

    return render(request, template, context)


def post_delete(request, id=None, template_name='blog/post_delete.html'):
    """Deleting individual item"""

    delete_query = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        delete_query.delete()
        return redirect('list')

    return render(request, template_name, {'delete_query':delete_query})




