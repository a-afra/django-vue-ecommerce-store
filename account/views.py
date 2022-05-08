import json

# Create your views here.
from djoser.conf import User
from djoser.serializers import UserSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class UserInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.filter(id=request.user.id)
        serializer = UserSerializer(user, many=True)
        return Response(json.loads(json.dumps(serializer.data))[0])
