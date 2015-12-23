
from django.conf.urls import include, url
from drip.views import UnsubscribeView

urlpatterns = [
    url(r'^unsubscribe/$', UnsubscribeView.as_view(), name='unsubscribe')
]
