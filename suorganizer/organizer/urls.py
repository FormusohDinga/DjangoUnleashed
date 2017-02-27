from django.conf.urls import url

from .views import (tag_detail, tag_list, startup_list)

urlpatterns = [
    url(r'^tag/$', tag_list, name="organizer_tag_list" ),
    url(r'^tag/(?P<slug>[\w\-]+)/$',tag_detail, name="organizer_tag_detail"),
    url(r'^startup/$', startup_list, name="organizer_startup_list"),
]
