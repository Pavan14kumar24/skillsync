from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Skill, Course, CourseProgress

# Home View
def home(request):
    skills = Skill.objects.all()
    courses = Course.objects.all()
    return render(request, 'core/home.html', {'skills': skills, 'courses': courses})

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'core/signup.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'core/signup.html')

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})

    return render(request, 'core/login.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('home')

# Course List View
@login_required
def course_list(request):
    user = request.user
    courses = Course.objects.all()

    # Fetch progress for this user
    course_progress_map = {}
    for course in courses:
        progress_entry, _ = CourseProgress.objects.get_or_create(user=user, course=course)
        course_progress_map[course.id] = progress_entry.progress

    return render(request, 'core/courses.html', {
        'courses': courses,
        'course_progress_map': course_progress_map
    })

# Update Progress View
@login_required
def update_progress(request, course_id):
    if request.method == 'POST':
        new_progress = int(request.POST.get('progress', 0))
        course = get_object_or_404(Course, id=course_id)

        progress_entry, _ = CourseProgress.objects.get_or_create(user=request.user, course=course)
        progress_entry.progress = new_progress
        progress_entry.save()

    return redirect('course_list')