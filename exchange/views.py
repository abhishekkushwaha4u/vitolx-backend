from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from exchange.models import (
    Exchange
)
from product.models import (
    Product
)
from user.models import (
    UserNotification
)
import os
import requests

class ProductExchangeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        product_id = request.query_params.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            Exchange.objects.create(
                buyer=request.user,
                product=product
            )
            notification_check = UserNotification.objects.filter(user=product.owner)
            if notification_check:
                chat_id = notification_check[0].token
            else:
                return Response({"error":"unable to create exchange due to token not being added"}, status=403)
            token = os.environ.get('TELEGRAM_TOKEN')
            message = "Hi! You have a product exchange request from {}. You can contact him on {}".format(product.owner.full_name, product.owner.userprofile.phone_number)
            response = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}')
            print(response.json())
            return Response({"message": "Notification sent successfully!"})
        except Exception as e:
            print(e)
            return Response({"error":"unable to create exchange"}, status=403)
