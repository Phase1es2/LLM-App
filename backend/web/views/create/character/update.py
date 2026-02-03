from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.utils.timezone import now
from web.models.character import Character
from web.views.utils.photo import remove_old_photos


class UpdateCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
             #__ 获取关联元素
            character = Character.objects.get(id=character_id, author__user=request.user)
            name = request.data['name'].strip()
            profile = request.data['profile'].strip()[:100000]
            photo = request.FILES.get('photo', None)
            background_image = request.FILES.get('background_image', None)

            if not name:
                 return Response({'result': 'name is required'})
            if not profile:
                 return Response({'result': 'profile is required'})
            if photo:
                 remove_old_photos(character.photo)
                 character.photo = photo
            if background_image:
                remove_old_photos(character.background_image)
                character.background_image = background_image

            character.name = name
            character.profile = profile
            character.update_time = now()
            character.save()
            return Response({
                'result': 'success',
            })
        except:
            return Response({
                'result': 'system error, try again later',
            })