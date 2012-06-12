from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^studies/$', 'studies.views.home'),
    url(r'^studies/GSE(?P<studynumber>\d+)/$', 'studies.views.data'),
    url(r'^studies/list/$', 'studies.views.list'),
    url(r'^studies/submitted/$', 'studies.view.thanks'),
    url(r'^studies/plist/$', 'studies.views.plist'),
    url(r'^studies/qlist/$', 'studies.views.qlist'),
    url(r'^studies/about/$', 'studies.views.about'),
    url(r'^studies/download/GSE(?P<studynumber>\d+)/$', 'studies.views.send_zipfile'),
    url(r'^studies/getData/$', 'studies.views.formatData'),
    url(r'^studies/downloadAllPairs/GSE(?P<studynumber>\d+)/$', 'studies.views.sendAllPairs'),
    url(r'^studies/downloadLog/GSE(?P<studynumber>\d+)/$', 'studies.views.sendLog'),

)
