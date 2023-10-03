from django.urls import reverse, path
from . import views

urlpatterns = [
    path('', views.help),
    path('lessons/<int:userid>', views.users_allowed_lessons)
]