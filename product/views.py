from django.shortcuts import render
from rest_framework.views import APIView
from .serialiser import ProductSerialiser
from .models import Product
from django.http import JsonResponse

# Create your views here.
model=Product
class ProductView(APIView):
    def get(self,request): #get one product or all products
       pid=request.GET.get('id',None)
       if pid is not None:
              product=model.objects.get(id=pid)
              serializer=ProductSerialiser(product)
              return JsonResponse(serializer.data)
       else:
            products=model.objects.all()
            serializer=ProductSerialiser(products,many=True)
            return JsonResponse(serializer.data,safe=False)
       
    def post(self,request): #add product
        serializer=ProductSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Product added'})
        else:
            return JsonResponse({'message':'Product addition failed'})
        
    def put(self,request): #update product
        product=model.objects.get(id=request.data['id'])
        serializer=ProductSerialiser(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Product updated'})
        else:
            return JsonResponse({'message':'Product updation failed'})
    
    def delete(self,request):
        id=request.data['id']
        product=model.objects.get(id=id)
        product.delete()
        return JsonResponse({'message':'Product deleted'})
    
         