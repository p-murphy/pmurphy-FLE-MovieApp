from django.conf.urls import patterns, include, url

from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(__package__ + '.views',
	url(r'^$', 'index', name='index'),
	url(r'^details/(?P<movie_id>\d+)/$', 'details', name='details'),
	url(r'^search/$', 'search', name='search'),
	url(r'^about/$', 'about', name='about'),
    url(r'^$', 'landing_page', {}, 'landing_page'),
    url(r'^admin/', include(admin.site.urls)),
)
