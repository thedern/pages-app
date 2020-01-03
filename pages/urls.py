from django.urls import path

# import the class
from .views import HomePageView, AboutPageView

# as_view() is a class method
# optional 'name' allows for anchors in our templates when using django template engine
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]