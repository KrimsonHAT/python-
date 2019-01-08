from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.ListProjects.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
]