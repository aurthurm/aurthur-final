from django.shortcuts import render
from django.views.generic import ListView, DetailView
from showcase.models import Portfolio


class PortfolioList(ListView):
	model = Portfolio
	context_object_name = 'portfolios'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class PortfolioDetail(DetailView):
	model = Portfolio
	pk_url_kwarg = 'portfolio_id'
	slug_url_kwarg = 'portfolio_slug'
	# query_pk_and_slug = True
	context_object_name = 'portfolio'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
