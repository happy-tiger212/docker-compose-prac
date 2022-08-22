from django.urls import path

from .views import GreetingView

urlpatterns = [
    path('', GreetingView.as_view())
]