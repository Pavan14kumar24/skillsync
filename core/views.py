from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Skill, Course, CourseProgress, SkillProficiency
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
import weasyprint
from .models import Feedback
from django.contrib import messages

# Home View
def home(request):
    skills = Skill.objects.all()
    courses = Course.objects.all()

    skill_proficiency_map = {}
    if request.user.is_authenticated:
        for skill in skills:
            prof_entry, _ = SkillProficiency.objects.get_or_create(user=request.user, skill=skill)
            skill_proficiency_map[skill.id] = prof_entry.proficiency

    return render(request, 'core/home.html', {
        'skills': skills,
        'courses': courses,
        'skill_proficiency_map': skill_proficiency_map
    })

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

    # Handle search
    query = request.GET.get('search')
    if query:
        courses = courses.filter(title__icontains=query)

    # Handle platform filter
    platform = request.GET.get('platform')
    if platform and platform != 'All':
        courses = courses.filter(platform__iexact=platform)

    # Prepare course progress map
    course_progress_map = {}
    completed_courses = []
    for course in courses:
        progress_entry, _ = CourseProgress.objects.get_or_create(user=user, course=course)
        course_progress_map[course.id] = progress_entry.progress
        if progress_entry.progress == 100:
            completed_courses.append(course.id)

    # List of unique platforms for filtering
    platforms = Course.objects.values_list('platform', flat=True).distinct()

    return render(request, 'core/courses.html', {
        'courses': courses,
        'course_progress_map': course_progress_map,
        'completed_courses': completed_courses,
        'platforms': platforms,
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

# Update Skill Proficiency View
@login_required
def update_proficiency(request, skill_id):
    if request.method == 'POST':
        new_prof = int(request.POST.get('proficiency', 0))
        skill = get_object_or_404(Skill, id=skill_id)

        prof_entry, _ = SkillProficiency.objects.get_or_create(user=request.user, skill=skill)
        prof_entry.proficiency = new_prof
        prof_entry.save()

    return redirect('home')


@login_required
def profile_dashboard(request):
    user = request.user
    skills = Skill.objects.all()
    courses = Course.objects.all()
    skill_progress = SkillProficiency.objects.filter(user=user)
    course_progress = CourseProgress.objects.filter(user=user)

    return render(request, 'core/profile.html', {
        'user': user,
        'skills': skills,
        'courses': courses,
        'skill_progress': skill_progress,
        'course_progress': course_progress,
    })


@login_required
def download_pdf(request):
    user = request.user
    skills = Skill.objects.all()
    courses = Course.objects.all()

    skill_data = [
        (skill.name, SkillProficiency.objects.filter(user=user, skill=skill).first().proficiency if SkillProficiency.objects.filter(user=user, skill=skill).exists() else 0)
        for skill in skills
    ]
    course_data = [
        (course.title, CourseProgress.objects.filter(user=user, course=course).first().progress if CourseProgress.objects.filter(user=user, course=course).exists() else 0)
        for course in courses
    ]

    html = get_template("core/pdf_template.html").render({
        'user': user,
        'skill_data': skill_data,
        'course_data': course_data
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; filename=report.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response

@login_required
def submit_feedback(request):
    if request.method == "POST":
        message = request.POST.get('message', '').strip()
        if message:
            Feedback.objects.create(user=request.user, message=message)
            messages.success(request, "Thank you for your feedback!")
        else:
            messages.error(request, "Feedback cannot be empty.")
        return redirect('home')
    