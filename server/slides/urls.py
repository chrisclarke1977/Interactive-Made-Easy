from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('slides.views',
    (r'^add/(?P<id>[^/]*)$', 'add_slide', {}, 'add_slide'),
    (r'^list/(?P<id>[^/]*)$', 'slide', {}, 'slide'),
)
