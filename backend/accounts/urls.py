from django.urls import path
from accounts.views import GithubLogin

urlpatterns = [
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login')
]
