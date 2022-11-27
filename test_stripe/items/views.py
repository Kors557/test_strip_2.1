import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv

from .models import Item

load_dotenv()


stripe.api_key = os.getenv('SK_STRIPE')


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        DOMAIN = os.getenv('DOMAIN')
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/'
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def get_item(request, **kwargs):
    item = Item.objects.get(id=kwargs['pk'])
    context = {
        'item': item,
        "STRIPE_PUBLIC_KEY": os.getenv('PK_STRIPE')
        }
    return render(request, 'landing.html', context)
