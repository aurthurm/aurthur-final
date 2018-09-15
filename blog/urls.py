from django.contrib import admin
from django.urls import path, include

# Customise url here if need arises
blog_urls = ([
    path('', include('zinnia.urls.capabilities')),
    path('search/', include('zinnia.urls.search')),
    path('sitemap/', include('zinnia.urls.sitemap')),
    path('trackback/', include('zinnia.urls.trackback')),
    path('blog/tags/', include('zinnia.urls.tags')),
    path('blog/feeds/', include('zinnia.urls.feeds')),
    path('blog/random/', include('zinnia.urls.random')),
    path('blog/authors/', include('zinnia.urls.authors')),
    path('blog/categories/', include('zinnia.urls.categories')),
    path('blog/comments/', include('zinnia.urls.comments')),
    path('blog/', include('zinnia.urls.entries')),
    path('blog/', include('zinnia.urls.archives')),
    path('blog/', include('zinnia.urls.shortlink')),
    path('blog/', include('zinnia.urls.quick_entry'))
], 'zinnia')

urlpatterns = [
    path('', include('zinnia.urls')), # direclty from zinnia
    # path('', include(blog_urls)), # if you wanna customise the url
]

