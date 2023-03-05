from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def walletPage(request):
    if request.method == 'POST':
        form = ppgPay(request.POST)
        if form.is_valid():
            queryset = walletDB.objects.filter(card_no=form.cleaned_data['card_no'])
            if queryset.exists():
                money = queryset.first().purse_amt
                queryset.update(purse_amt = money+form.cleaned_data['amount'])
            else:
                review = walletDB(
                    card_holder = form.cleaned_data['card_holder'],
                    card_no = form.cleaned_data['card_no'],
                    purse_amt = form.cleaned_data['amount']
                )
                review.save()
    form = ppgPay()
    return render(request, 'vtopwallet/wallet.html', {
        'form':form,
    })