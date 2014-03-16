from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from filebrowser.sites import site as filebrowser_site

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stage.views.home', name='home'),
    # url(r'^stage/', include('stage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(filebrowser_site.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Basic Apps dependencies
    # (r'^comments/', include('django.contrib.comments.urls')),
    # Basic Apps
    url(r'^blog/', include('basic.blog.urls')),
    url(r'^bookmarks/', include('basic.bookmarks.urls')),
    url(r'^books/', include('basic.books.urls')),
    url(r'^comments/', include('basic.comments.urls')),
    url(r'^events/', include('basic.events.urls')),
    url(r'^flagging/', include('basic.flagging.urls')),
    url(r'^groups/', include('basic.groups.urls')),
    url(r'^invitations/', include('basic.invitations.urls')),
    url(r'^photos', include('basic.media.urls.photos')),
    url(r'^videos', include('basic.media.urls.videos')),
    url(r'^messages/', include('basic.messages.urls')),
    url(r'^movies/', include('basic.movies.urls')),
    url(r'^music/', include('basic.music.urls')),
    url(r'^people/', include('basic.people.urls')),
    url(r'^places/', include('basic.places.urls')),
    url(r'^users/', include('basic.profiles.urls')),
    url(r'^relationships/', include('basic.relationships.urls')),
    # url(r'^tools/', include('basic.tools.urls')),
    # Apps
    url(r'^player/', include('player.urls')),
    url(r'^torrent/', include('torrent.urls')),
    url(r'^', include('base.urls')),
    # Login
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

from django.conf import settings

if settings.DEBUG:
    from django.views.static import serve
    if settings.MEDIA_URL.startswith('/'):
        media_url = settings.MEDIA_URL[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % media_url, serve,
                                 {'document_root': settings.MEDIA_ROOT}))
