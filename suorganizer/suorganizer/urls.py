from django.conf.urls import include, url
from django.contrib import admin

from organizer import urls as organizer_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(organizer_urls))
]
