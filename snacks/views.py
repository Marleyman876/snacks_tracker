from django.db import models
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'
  
class AboutView(TemplateView):
  template_name = 'about.html'
  
class SnackDetailsView(DetailView):
  template_name = 'snack_detail.html'
  models = Snack
  
class SnackListviews(ListView):
  template_name = 'snack_list.html'
  models = Snack
  