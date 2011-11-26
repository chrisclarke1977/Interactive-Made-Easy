from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('slides.views',
    (r'^add$', 'add_slide', {}, 'add_slide'),
    (r'^(?P<id>[^/]*)$', 'slide', {}, 'slide'),
)
