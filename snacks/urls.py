from django.urls import path
from .views import SnackListViews, SnackDetailsViews

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    # path('about/', AboutView.as_view(), name='about'),
    path('', SnackListViews.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailsViews.as_view(), name='snack_detail'),
]