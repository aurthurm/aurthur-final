from django.urls import path, include
from .views import PortfolioList, PortfolioDetail

app_name = 'showcase' # Portfolio
urlpatterns = [
    path('', PortfolioList.as_view(), name='portfolio-listing'),
    path('detail/<int:portfolio_id>/<slug:portfolio_slug>', PortfolioDetail.as_view(), name='portfolio-detail'),
]
