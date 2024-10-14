from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'learning/home.html')  # This view renders the home page

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'learning/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # or wherever you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'learning/login.html', {'form': form})

# View to list all courses
def courses(request):
    courses = [
        {'title': 'Basics of Python', 'description': 'Learn the essentials of Python programming. Get ready to build your first Python program.', 'url': 'basic-python'},
        
        {'title': 'Intermediate Python', 'description': 'Advance your Python skills with more complex concepts.', 'url': 'intermediate-python'},
        
        {'title': 'Advanced Python', 'description': 'Dive deep into advanced Python concepts and techniques to become a Python expert.', 'url': 'advanced-python'},

        

    ]
    return render(request, 'learning/courses.html', {'courses': courses})

# View for each individual course page
def basic_python(request):
    return render(request, 'learning/basic_python.html')

def intermediate_python(request):
    return render(request, 'learning/intermediate_python.html')


def advanced_python(request):
    return render(request, 'learning/advanced_python.html')



