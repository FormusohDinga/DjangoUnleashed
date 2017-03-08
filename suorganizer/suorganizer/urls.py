from django.conf.urls import include, url
from django.contrib import admin

from blog import urls as blog_urls
from contact import urls as contact_urls
from organizer.urls import (
    newslink as newslink_urls,
    startup as startup_urls, tag as tag_urls)
from django.contrib.auth import urls as auth_urls
from django.views.generic import (
    RedirectView, TemplateView)
from user import urls as user_urls
urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            pattern_name='blog_post_list',
            permanent=False)),
    url(r'^about/$',
        TemplateView.as_view(
            template_name='site/about.html'),
        name='about_site'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^newslink/', include(newslink_urls)),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),
    url(r'^user/', include(user_urls, app_name='user', namespace='dj-auth')),
]
