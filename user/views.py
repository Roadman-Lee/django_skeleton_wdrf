from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserCreateSerializer, UserSerializer


class UserApiView(APIView):

    # 로그인 유저 정보, 글 가져오기
    def get(self, request):
        user = request.user
        serialized_user_data = UserSerializer(user).data
        return Response(serialized_user_data)

    # 사용자 생성
    def post(self, request):
        user_create_serializer = UserCreateSerializer(data=request.data)

        if user_create_serializer.is_valid():
            user_create_serializer.save()
            return Response(user_create_serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            user_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
