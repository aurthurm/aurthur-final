from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	headings = HomePageHeadings.objects.all()[0]
	services = ServicesEntry.objects.all()
	subjects = Subject.objects.all()
	teachings = TeachingEntry.objects.all()
	technologies = TechTools.objects.all()
	return(render(request, 'home/home.html', context={
			'is_home': True,
			'headings': headings,
			'services': services,
			'subjects': subjects,
			'teachings': teachings,
			'technologies': technologies,
		}))