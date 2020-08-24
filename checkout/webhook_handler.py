from django.http import HttpResponse


class StripeWH_Handler:
    """ Handling the Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling any other than standard webhook event """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
