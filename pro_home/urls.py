from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView

urlpatterns = [
    path("",views.home,name="home"),
    # path('accounts/login/', LoginView.as_view(), name='login'),
    path("sign-up/",views.index,name="index"),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('search_repositories/', views.search_repositories, name='search_repositories'),
]