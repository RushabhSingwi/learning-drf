from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


from .models import Blog, Author
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)
def blog_view(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)

def sign_up(request):
    if request.method == 'POST':
        data = request.POST
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password == confirm_password:
            Author.name=data.get('name'),
            Author.email=data.get('email'),
            Author.location=data.get('location'),
            Author.gender=data.get('gender')
            password=data.get('password')
            
            # Process signup
            # For example, create a new user object
            # Redirect to a success page or login page
            return redirect('signup.html')  # Replace 'success_page' with your URL name
        else:
            messages.error(request, 'Password does not match', extra_tags='unique')
            return render(request, 'signup.html')
           
    return render(request, 'signup.html')