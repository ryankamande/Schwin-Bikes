# from django.shortcuts import render
# from django.utils.decorators import method_decorator
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from django_daraja.mpesa.core import MpesaClient

# from store.forms import PaymentForm


# class MpesaPaymentView(View):
#     template_name = 'checkout.html'
#     form_class = PaymentForm

#     @method_decorator(csrf_exempt)  # Use this decorator for class-based views
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             client = MpesaClient()
#             user_phone_number = form.cleaned_data['phone']
#             # Format the phone number for M-Pesa API
#             phone_number = '254' + user_phone_number[1:]
#             amount = form.cleaned_data['amount']
#             account_reference = 'reference'
#             transaction_desc = 'CustomerPayBillOnline'
#             callback_url = 'https://de55-197-232-81-156.ngrok-free.app/callback'
#             response = client.stk_push(amount, phone_number, account_reference, transaction_desc, callback_url)

#             if response and response.get('ResponseCode') == '0':
#                 return render(request, self.template_name, {'form': form})
#             else:
#                 return render(request, 'Failed.html')

#         return render(request, self.template_name, {'form': form})