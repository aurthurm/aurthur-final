from django.urls import path, include
from .views import home

app_name = 'home'
urlpatterns = [
	# path('attachments/', include('attachments.urls', namespace='attachments')),
    path('', home, name='home' ),
]
