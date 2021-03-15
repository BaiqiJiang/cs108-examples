# file: pages/views.html
# description: provide a view to send to the user


from django.urls import path
from .views import HomePageView, AboutPageView, SchedulePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('schedule', SchedulePageView.as_view(), name='schedule'),
]