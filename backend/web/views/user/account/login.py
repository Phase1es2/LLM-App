from http.client import responses

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username').strip() # remove 前後空格
            password = request.data.get('password').strip()
            if not username or not password:
                return Response({
                    'result': 'username and password are required',
                })
            user = authenticate(username=username, password=password) # 驗證用戶名密碼是否匹配，匹配返回用戶名不匹配return None
            if user:
                user_profile = UserProfile.objects.get(username=username)
                refresh = RefreshToken.for_user(user) # create JWT
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )
                return response
            return Response({
                'result': 'username or password incorrect',
            })
        except:
            return Response({
                'result': 'error, please try again later',
            })
