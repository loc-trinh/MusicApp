from django.conf.urls import patterns, include, url
from django.contrib import admin
from YTD import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.youtube, name="youtube"),
    url(r'^frame/$', views.frame, name="frame"),
)
