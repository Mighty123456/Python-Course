from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import sys
import os

# Add the parent directory to the Python path to import views
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
