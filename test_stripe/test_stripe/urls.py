from django.contrib import admin
from django.urls import path
from items.views import CreateCheckoutSessionView, get_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<pk>/', get_item, name='landing'),
    path(
        'buy/<pk>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    ),
]
