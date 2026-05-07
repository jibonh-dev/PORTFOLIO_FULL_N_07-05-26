from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('resume/', views.resume_view, name='resume'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Profile
    path('dashboard/profile/', views.profile_edit, name='profile_edit'),

    # Skills
    path('dashboard/skill/add/', views.skill_add, name='skill_add'),
    path('dashboard/skill/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('dashboard/skill/<int:pk>/delete/', views.skill_delete, name='skill_delete'),

    # Projects
    path('dashboard/project/add/', views.project_add, name='project_add'),
    path('dashboard/project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('dashboard/project/<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Experience
    path('dashboard/experience/add/', views.experience_add, name='experience_add'),
    path('dashboard/experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    path('dashboard/experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),

    # Education
    path('dashboard/education/add/', views.education_add, name='education_add'),
    path('dashboard/education/<int:pk>/edit/', views.education_edit, name='education_edit'),
    path('dashboard/education/<int:pk>/delete/', views.education_delete, name='education_delete'),
]
