# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path # URL routing
from .views import home,login_page,register_page


# Define URL patterns
urlpatterns = [
	path('home/', home, name="recipes"),	 # Home page		
	path('', login_page, name='login_page'), # Login page
	path('register/', register_page, name='register'), # Registration page
]

# Serve media files if DEBUG is True (development mode)

