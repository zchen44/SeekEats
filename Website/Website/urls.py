"""
Definition of urls for Website.
"""

from django.urls import include, path
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Website.views.home, name='home'),
    # url(r'^Website/', include('Website.Website.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
