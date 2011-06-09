from django.conf.urls.defaults import *
import settings

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', 'main.views.hello'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.STATIC_DOC_ROOT}),
)
