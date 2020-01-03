from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class-based view approached (as opposed to function-based views like in flask)


class HomePageView(TemplateView):
    # subclass template view
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

