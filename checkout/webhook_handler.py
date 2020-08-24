from django.http import HttpResponse


class StripeWH_Handler:
    """ Handling the Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handling any other than standard webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handling payment_intent.succeeded webhook by Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handling payment_intent.payment_failed webhook by Stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
