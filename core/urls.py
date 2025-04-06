from django.urls import path
from core import views
from core.views import course_list, update_progress

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Course progress tracking URLs
    path('courses/', course_list, name='course_list'),
    path('update-progress/<int:course_id>/', update_progress, name='update_progress'),
]