from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# same app
from user_auth.forms import SignUpForm, ProfileForm
from user_auth.models import Profile


def sign_up(request):
    """Signup View"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return redirect('profile-create')
                    template = 'user_auth/profile.html'
                    # messages.success(request, 'Your account has been created! You are now Logged in')
                    return render(request, template)
    else:
        form = SignUpForm()

    template = 'user_auth/signup.html'
    context = {'form':form}
    return render(request, template, context)


@login_required(login_url='login')
def profile(request):
    """See Profile"""
    template = 'user_auth/profile.html'
    return render(request, template)


@login_required(login_url='login')
def profile_create(request):
    """Create Profile"""


    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # messages.success(request, 'Your Profile has been created!')
            return redirect('profile-detail', id=profile.id)
            # return redirect('profile-detail', id=profile.id)

    context = {
        'form': ProfileForm(),
    }

    template = 'user_auth/profile_create.html'

    return render(request, template, context)


@login_required(login_url='login')
def profile_detail(request, id=None):
    """See Profile Details"""
    profile = get_object_or_404(Profile, id=id)
    context = {'profile': profile}
    template = 'user_auth/profile_detail.html'

    return render(request, template, context)


@login_required(login_url='login')
def profile_edit(request):
    """Edit Profile"""
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # messages.success(request, 'Your Profile has been Updated!')
            return redirect('user/profile-detail/')

    context = {'form':form}
    template = 'user_auth/profile_edit.html'

    return render(request, template, context)



