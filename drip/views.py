
from django.views.generic import View
from django.http import HttpResponse, Http404
from drip.models import Subscription

class UnsubscribeView(View):
    def get(self, request):
        c = request.GET.get('code')
        if not c:
            raise Http404('Sorry, this unsubscribe link is not valid.')
        sub = Subscription.for_unsubscribe_code(c)
        if sub is None:
            raise Http404('Unknown unsubscribe code.')

        sub.unsubscribed = True
        sub.save()
        return HttpResponse('Unsubscribed! You will no longer receive these ' \
                            'emails from us.')
