from django.conf.urls import url
from django.test import TestCase
from django.http import response
from django.urls import reverse

# Create your tests here.

class Snacks_Test(TestCase):
  
  def test_snack_page_status(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_snack_list(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'snack_list.html')    
  
  
  # def test_home_page(self):
  #   url = reverse('home')
  #   response = self.client.get(url)
  #   self.assertEqual(response.status_code, 200)
    
  # def test_about_page(self):
  #   url = reverse('about')
  #   response = self.client.get(url)
  #   self.assertEqual(response.status_code, 200)
    
  # def test_homepage(self):
  #   url = reverse('home')
  #   response = self.client.get(url)
  #   self.assertTemplateUsed(response, 'home.html')
  #   self.assertTemplateUsed(response, 'base.html')
    
  # def test_about_page_code(self):
  #   url = reverse('home')
  #   response = self.client.get(url)
  #   self.assertEqual(response.status_code, 200)
    