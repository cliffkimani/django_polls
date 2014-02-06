from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import redirect2polls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', redirect2polls),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),  # note the lack of a terminal dollar sign in the re
    url(r'^admin/', include(admin.site.urls)),
)
