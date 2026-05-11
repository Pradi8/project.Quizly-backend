from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegistrationView(APIView):
    """
    API endpoint for user registration.
    - Allows any user (no authentication required)
    - Accepts POST request with: fullname, email, password, repeated_password
    - Returns token and user info on successful registration
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data = {
                "detail": "User created successfully!"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CookieTokenObtainPairView(TokenObtainPairView):
   
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
     
        access = serializer.validated_data["access"]
        refresh = serializer.validated_data["refresh"]

        response = Response({
            "detail": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        })

        response.set_cookie(
            key="access_token",
            value=str(access),
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,
            samesite="Lax"
        )
        
        return response
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response({"detail": "Log-Out successfully! All Tokens will be deleted. Refresh token is now invalid."}, status=status.HTTP_200_OK)

        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
    
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            return Response(
                {"error": "Refresh token not provided"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response(
                {"error": "Invalid refresh token"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        access_token = serializer.validated_data.get("access")

        response = Response({"detail": "Token refreshed"})

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        return response