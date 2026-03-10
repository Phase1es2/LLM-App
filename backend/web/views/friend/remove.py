from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend


class RemoveFriendView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            friend_id = request.data['friend_id']
            # USER IN ME == USER ME__USER
            Friend.objects.filter(id=friend_id, me__user=request.user).delete()
            return Response ({
                'result': 'success',
            })
        except:
            return Response ({
                'result': 'system error, please try again later',
            })