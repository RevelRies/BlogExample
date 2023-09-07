from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'blog/home.html'


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'