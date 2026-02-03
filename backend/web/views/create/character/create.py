from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character
from web.models.user import UserProfile


class CreateCharacterAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            name = request.data.get('name').strip()
            profile = request.data.get('profile').strip()[:100000]
            photo = request.FILES.get('photo', None)
            background_image = request.FILES.get('background_image', None)
            if not name:
                return Response({'error': 'Name is required'})
            if not profile:
                return Response({'error': 'Profile is required'})
            if not photo:
                return Response({'error': 'Photo is required'})
            if not background_image:
                return Response({'error': 'Background image is required'})

            Character.objects.create(
                author=user_profile,
                name=name,
                profile=profile,
                photo=photo,
                background_image=background_image,
            )
            return Response({
                'success': 'success'
            })
        except:
            return Response({
                'result': 'system error, try again later',
            })