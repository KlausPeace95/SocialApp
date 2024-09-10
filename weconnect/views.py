from django.shortcuts import render, redirect
from .forms import PostsForm
from .models import Posts, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm

@login_required
def dashboard(request):
    form = PostsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            posts = form.save(commit=False)
            posts.user = request.user
            posts.save()
            return redirect("weconnect:dashboard")
    # form = PostsForm()
    followed_posts = Posts.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    context = {
        'form': form,
        'posts': followed_posts
    }
    return render(request, "weconnect/dashboard.html", context)

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {'profiles': profiles}
    return render(request, "weconnect/profile_list.html", context)

def profile(request, pk):
   if not hasattr(request.user, 'profile'):
       missing_profile = Profile(user=request.user)
       missing_profile.save()
   else:


    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    context = {'profile': profile}
    return render(request, "weconnect/profile.html", context)

def register(request):
    context = {'form': CustomUserCreationForm}
    if request.method == "GET":
        return render(request, "weconnect/register.html", context)
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("weconnect:dashboard"))


