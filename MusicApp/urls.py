from django.conf.urls import patterns, include, url
from django.contrib import admin
from YTD import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.youtube, name="youtube"),
    url(r'^frame/$', views.frame, name="frame"),
    url(r'^add_to_download/$', views.add_to_download_queue, name="add_to_download"),
    url(r'^downloads/$', views.downloads, name="downloads"),
    url(r'^download_video/$', views.download_video, name="download_video")
)
