from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from django.conf import settings
import requests

from api.serializers import UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

class UserCreateView(APIView):
    """
    API to Register New user
    Request_Body:
        first_name (Optinal) - First Name
        last_name (Optinal) - Last Name
        email (Optinal) - Email Name
        username (Required) - User Name (Unique)
        password (Required) - Password
    Response:
        Josn response
    """
    @swagger_auto_schema(
        request_body=UserCreateSerializer,  # This links the serializer to the request body
        responses={201: UserCreateSerializer}  # Response after successful creation
    )
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['get'],
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, description="Authorization header", type=openapi.TYPE_STRING),
    ]
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_coins_list(request):
    """
    API to get all coins list
    Response:
        Josn response
    """
    url = f"{settings.COIN_API_URL}/list/"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": settings.X_CG_DEMO_API_KEY
    }

    response = requests.get(url, headers=headers)
    return Response(
        {"coins_list": response.json()},
        status=status.HTTP_200_OK
    )
    



@swagger_auto_schema(
    methods=['get'],
    manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, description="Authorization header", type=openapi.TYPE_STRING),
    ]
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_coins_categories(request):
    """
    API to get all categories list
    Response:
        Josn response
    """
    url = f"{settings.COIN_API_URL}/categories/list/"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": settings.X_CG_DEMO_API_KEY
    }

    response = requests.get(url, headers=headers)
    return Response(
        {"coins_categories": response.json()},
        status=status.HTTP_200_OK
    )
    

@swagger_auto_schema(
    methods=['get'],
    manual_parameters=[
        openapi.Parameter('per_page', openapi.IN_QUERY, description="Pre Page Data (Default: 10)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page', openapi.IN_QUERY, description="Page (Default: 1)", type=openapi.TYPE_INTEGER),
        openapi.Parameter('coin_id', openapi.IN_QUERY, description="Coin ID e.g.:bitcoin, ethereum", type=openapi.TYPE_STRING),
        openapi.Parameter('category_id', openapi.IN_QUERY, description="Category ID e.g:t-chain-ecosystem,aave-tokens", type=openapi.TYPE_STRING),
        openapi.Parameter('currency', openapi.IN_QUERY, description="Currency (Default: cad)", type=openapi.TYPE_STRING),
        openapi.Parameter('Authorization', openapi.IN_HEADER, description="Authorization header", type=openapi.TYPE_STRING),
    ]
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_coins_markets(request):
    """
    API to get coins markets details
    Query_Params:
        per_page (default:10) - list of per page
        page (default:1) - page number
        coin_id (Optinal) - filter coins details ny coins id 
        category_id (Optinal) - filter coins details ny category id 

    Response:
        Josn response
    """
    coin_id = request.GET.get("coin_id")
    category_id = request.GET.get("category_id")
    per_page = request.GET.get("per_page", 10)
    page = request.GET.get("page", 1)
    currency = request.GET.get("currency", "cad")
    url = f"{settings.COIN_API_URL}/markets?vs_currency={currency}&per_page={per_page}&page={page}"
    if coin_id is not None:
        url += f"&ids={coin_id}"
    if category_id is not None:
        url += f"&category_id={category_id}"

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": settings.X_CG_DEMO_API_KEY
    }

    response = requests.get(url, headers=headers)
    return Response(
        {"coins_markets": response.json()},
        status=status.HTTP_200_OK
    )
    

