from django.shortcuts import render
from rest_framework.views import APIView
from .serialiser import WishlistSerialiser
from .models import Wishlist
from django.http import JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


model=Wishlist

class WishlistView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self,request): #get one product or all products
        userId=request.user.id
        wishes=model.objects.filter(userId=userId)
        serializer=WishlistSerialiser(wishes,many=True)
        return JsonResponse(serializer.data,safe=False)
       
    def post(self,request): #add product
        #get userid from token
        userId=request.user.id
        # print(userId)
        wish=Wishlist(userId=userId,productId=request.data['productId'])
        wish.save()
        return JsonResponse({'message':'Wish added'})
    
    def delete(self,request):
        id=request.data['id']
        wish=model.objects.get(id=id)
        wish.delete()
        return JsonResponse({'message':'wish deleted'})