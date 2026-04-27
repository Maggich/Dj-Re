from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return JsonResponse({
                "message": "ok",
                "user": user.username
            })

        return JsonResponse({"error": "invalid"}, status=400)


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session.save()

            return JsonResponse({
                "message": "register success",
                "username": user.username,
            }, status=201)

        return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "only POST"}, status=405)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "logout success"}, status=200)



    
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "not found"}, status=404)

        product.delete()
        return Response({"message": "deleted"}, status=204)