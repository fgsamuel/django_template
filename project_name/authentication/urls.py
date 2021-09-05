from django.urls import path

from {{ project_name }}.authentication.views import login_view, logout_view

app_name = 'auth'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
