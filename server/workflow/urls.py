from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('workflow.views',
    (r'^$', 'ajax', {}, 'workflow_ajax'),
    (r'^add$', 'add_workflow', {}, 'workflow'),
    #(r'^(?P<id>[^/]*)$', 'slide', {}, 'slide'),
)
