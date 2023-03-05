from django.urls import path
from . import views

urlpatterns = [
    path("wallet/", views.walletPage, name="wallet")
]