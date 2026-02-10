from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character
from web.views.utils.photo import remove_old_photos


class RemoveCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
            character = Character.objects.get(pk=character_id, author__user=request.user)
            # Character.objects.filter(pk=character_id, author__user=request.user).delete()
            remove_old_photos(character.photo)
            remove_old_photos(character.background_image)
            character.delete()
            return Response({
                'result': 'success',
            })
        except:
            return Response({
                'result': 'system error, try again later',
            })