from urllib.parse import urlparse
from django.urls import path

from accounts.views import CacheView

urlpatterns = [
    path('', CacheView.as_view()) 
]
