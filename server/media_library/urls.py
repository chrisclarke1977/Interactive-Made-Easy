from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('media_library.views',
    (r'^add$', 'add_media', {}, 'media'),
    #(r'^(?P<id>[^/]*)$', 'slide', {}, 'slide'),
)
