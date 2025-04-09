from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Course progress tracking
    path('courses/', views.course_list, name='course_list'),
    path('update-progress/<int:course_id>/', views.update_progress, name='update_progress'),
    

    # 🟢 FIXED: Match name to the view function
    path('update-skill/<int:skill_id>/', views.update_proficiency, name='update_proficiency'),
    path('profile/', views.profile_dashboard, name='profile'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]