# import base64

# import requests


# def initiate_mpesa_payment(amount, phone_number, account_reference, transaction_desc, callback_url):
#     # Replace with your API keys
#     consumer_key = 'On8lmwktWHRC5Z0frpnMQYbGM6zXGg38'
#     consumer_secret = 'xKGJbgibGFxZmX2A'
    

#     # M-Pesa API endpoint for initiating a payment
#     endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

#     headers = {
#         'Authorization': f'Bearer {get_access_token(consumer_key, consumer_secret)}',
#         'Content-Type': 'application/json'
#     }

#     payload = {
#         'BusinessShortCode': '174379',
#         'Password': 'MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMxMTI3MTIxNDI4',
#         'Timestamp': '20231127121428',
#         'TransactionType': 'CustomerPayBillOnline',
#         'Amount': amount,
#         'PartyA': phone_number,
#         'PartyB': '174379',
#         'PhoneNumber': phone_number,
#         'CallBackURL': 'https://de55-197-232-81-156.ngrok-free.app/callback',
#         'AccountReference': 'Apparel Fashion House',
#         'TransactionDesc': 'Payment for goods/services'
#     }
    
#     print("Request Payload:", payload)
#     response = requests.post(endpoint, json=payload, headers=headers)
#     print("Response Status Code:", response.status_code)
#     if response.status_code == 200:
#         # Payment request successful, handle the response
#         print("Response JSON:", response.json())
#         return response.json()
#     else:
#         print("Error Response:", response.text)
#         # Handle error
#         return None


# def get_access_token(consumer_key, consumer_secret):
#     # M-Pesa API endpoint for getting an access token
#     endpoint = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

#     credentials = base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode('utf-8')).decode('utf-8')
#     headers = {
#         'Authorization': f'Basic {credentials}'
#     }

#     response = requests.get(endpoint, headers=headers)

#     if response.status_code == 200:
#         # Access token obtained successfully
#         return response.json()['access_token']
#     else:
#         # Handle error
#         return None
