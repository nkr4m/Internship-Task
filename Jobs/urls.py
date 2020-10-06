from django.urls import path
from .views import JOBS
urlpatterns = [
path('', JOBS.as_view()),
]