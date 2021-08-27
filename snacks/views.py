from django.db import models
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snacks

# Create your views here.

# class HomeView(TemplateView):
#   template_name = 'home.html'
  
# class AboutView(TemplateView):
#   template_name = 'about.html'
  
class SnackDetailsViews(DetailView):
  template_name = 'snack_detail.html'
  model = Snacks
  
class SnackListViews(ListView):
  template_name = 'snack_list.html'
  model = Snacks
  