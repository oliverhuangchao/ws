from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import *
#needed
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^index/$', base),
    (r'^login/$', login),
    (r'^logout/$', logout),

    (r'^register/$', register),
    # (r'^blog/$', blog),

    (r'^search/$', search), # test query 

    (r'^registerFormSubmit/$', registerCheck),
    (r'^loginFormSubmit/$', loginCheck),
    #(r'^browser/$', browser),
    (r'^upload/$', upload),
    (r'^uploadProcess/$', uploadProcess),

    (r'^returnToUserMain/$', returnToUserMain),
    (r'^returnToMain/$', returnToMain),

    (r'^test/$', test),

    (r'^mediaClick/$', mediaClick),
    (r'^mediaDelete/$', mediaDelete),

    (r'^edit/$', edit),
    (r'^editUpdate/$', editUpdate),

    (r'^allMediaBrowser/$', allMediaBrowser),
    (r'^imageBrowser/$', imageBrowser),
    (r'^videoBrowser/$', videoBrowser),
    (r'^audioBrowser/$', audioBrowser),

    (r'^metaUpdate/$', metaUpdate),


)
