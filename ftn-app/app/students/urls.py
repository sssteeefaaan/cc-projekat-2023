from django.urls import path
from django.views.generic.base import RedirectView

from .views import register, profile

urlpatterns = [
    path('register/', view=register, name='student-register'),
    path('profile/<username>', view=profile, name='student-profile'),
    path('', RedirectView.as_view(url="/students/register"))
]
