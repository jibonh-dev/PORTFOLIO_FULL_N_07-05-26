from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, Education, Contact
from .forms import (LoginForm, RegisterForm, ContactForm, ProfileForm,
                    SkillForm, ProjectForm, ExperienceForm, EducationForm)


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'portfolio/home.html', {
        'profile': profile, 'skills': skills,
        'projects': projects, 'experiences': experiences, 'educations': educations,
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # allow login with email
        if '@' in username:
            try:
                username = User.objects.get(email=username).username
            except User.DoesNotExist:
                pass
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'portfolio/login.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        login(request, user)
        return redirect('dashboard')
    return render(request, 'portfolio/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'portfolio/contact.html', {'form': form})


def resume_view(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    return render(request, 'portfolio/resume.html', {
        'profile': profile, 'skills': skills,
        'experiences': experiences, 'educations': educations,
    })


@login_required
def dashboard(request):
    return render(request, 'portfolio/dashboard.html', {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'contacts': Contact.objects.all().order_by('-sent_at'),
    })


# ── Profile ──────────────────────────────────────────────
@login_required
def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, 'Profile updated.')
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Profile'})


# ── Skill ─────────────────────────────────────────────────
@login_required
def skill_add(request):
    form = SkillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Skill'})


@login_required
def skill_edit(request, pk):
    obj = get_object_or_404(Skill, pk=pk)
    form = SkillForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Skill'})


@login_required
def skill_delete(request, pk):
    get_object_or_404(Skill, pk=pk).delete()
    return redirect('dashboard')


# ── Project ───────────────────────────────────────────────
@login_required
def project_add(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Project'})


@login_required
def project_edit(request, pk):
    obj = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Project'})


@login_required
def project_delete(request, pk):
    get_object_or_404(Project, pk=pk).delete()
    return redirect('dashboard')


# ── Experience ────────────────────────────────────────────
@login_required
def experience_add(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Experience'})


@login_required
def experience_edit(request, pk):
    obj = get_object_or_404(Experience, pk=pk)
    form = ExperienceForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Experience'})


@login_required
def experience_delete(request, pk):
    get_object_or_404(Experience, pk=pk).delete()
    return redirect('dashboard')


# ── Education ─────────────────────────────────────────────
@login_required
def education_add(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Add Education'})


@login_required
def education_edit(request, pk):
    obj = get_object_or_404(Education, pk=pk)
    form = EducationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Edit Education'})


@login_required
def education_delete(request, pk):
    get_object_or_404(Education, pk=pk).delete()
    return redirect('dashboard')
