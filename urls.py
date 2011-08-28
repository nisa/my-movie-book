from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite.movies.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'home_page'),
    (r'^accounts/signup/$', 'register'),
    url(r'^accounts/profile/$', 'movies_list',name="movies_list"),
    (r'^add_movie/$', 'add_movie'),
    (r'^delete_movie/(\d+)$', 'delete_movie'),
    (r'^accounts/signup/next/$', 'signup_next'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^accounts/login/$', 'login',name="login"),
    url(r'^accounts/logout/$','logout',name="logout"),
)	
