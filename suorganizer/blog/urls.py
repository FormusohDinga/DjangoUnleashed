from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (
    PostCreate, PostDelete, PostList, PostUpdate,
    PostDetail, PostArchiveYear)

urlpatterns = [
    url(r'^$',
        PostList.as_view(),
        name='blog_post_list'),
    url(r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'),
    url(r'^(?P<year>\d{4})/$',
        PostArchiveYear.as_view(),
        name='blog_post_archive_year'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<day>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        PostDetail.as_view(),
        name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'delete/$',
        PostDelete.as_view(),
        name='blog_post_delete'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'update/$',
        PostUpdate.as_view(),
        name='blog_post_update'),
]
