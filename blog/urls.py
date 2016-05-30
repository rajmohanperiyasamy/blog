from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'snap.views.display_article', name='home'),
    url(r'^$', 'blog.views.gale_task', name='home'),
    url(r'^detail/(?P<pk>\d+)$', 'blog.views.detail', name='detail'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
