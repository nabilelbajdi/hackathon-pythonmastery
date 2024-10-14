from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import built-in auth views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='learning/login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Logout page
    path('courses/', views.courses, name='courses'),
    path('courses/basic-python/', views.basic_python, name='basic-python'),
<<<<<<< Updated upstream
=======
    path('courses/advanced-python/', views.advanced_python, name='advanced-python'),
    path('resources/', views.resources, name='resources'),
>>>>>>> Stashed changes
]
