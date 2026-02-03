from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated #must login

from web.models.user import UserProfile
from web.views.utils.photo import remove_old_photos


class UpdateProfileView(APIView):
    # make sure it is logined in
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            # get(gt 1 and eq 0 create err) and filter(list)
            username = request.data.get('username').strip()
            profile = request.data.get('profile').strip()[:500]
            photo = request.FILES.get('photo', None)
            if not username:
                return Response({
                    'result': 'username is required',
                })
            if not profile:
                return Response({
                    'result': 'profile is required',
                })
            if username != user.username and User.objects.filter(username=username).exists():
                return Response({
                    'result': 'username is already taken',
                })
            if photo:
                remove_old_photos(user_profile.photo)
                user_profile.photo = photo
            user_profile.profile = profile
            user_profile.update_time = now()
            user_profile.save()
            user.username = username
            user.save()
            return Response({
                'result': 'success',
                'user_id': user.id,
                'username': user.username,
                'profile': user_profile.profile,
                'photo': user_profile.photo.url,
            })
        except:
            return Response({
                'result': "system error, try again later",
            })
