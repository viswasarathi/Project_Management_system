from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# from .forms import RepositoryForm
# from .models import UserProfile
# from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"home.html")


def index(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']

    #     user = User.objects.create_user(username=username,email=email,password=password)
    #     user.save()
    return render(request,"index.html")


# @login_required
# def dashboard(request):
#     # Assuming you have a UserProfile model related to the User
#     user_details = UserProfile.objects.get(user=request.user)
#     form = RepositoryForm()

#     if request.method == 'POST':
#         form = RepositoryForm(request.POST)
#         if form.is_valid():
#             repo = form.save(commit=False)
#             repo.creator = request.user
#             repo.save()
#             return redirect('dashboard')

#     context = {
#         'user_details': user_details,
#         'form': form
#     }
#     return render(request, 'main_app/dashboard.html', context)

# def search_repositories(request):
#     # Implement search repositories functionality here
#     return render(request, 'main_app/search_repositories.html')

        

       
    # else:
    #     return render(request,"index.html")