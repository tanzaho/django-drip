
from django.conf.urls import include, url

urlpatterns = [
    url(r'^unsubscribe/$', UnsubscribeView.as_view(), name='unsubscribe')
]
