from django.contrib.auth import authenticate, login
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserProfile
from user.serializers import UserSerializer, UserProfileSerializer


class VerifyPermissionLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_level >= 0)
        return result


class UserApiView(APIView):
    # permission_classes = [VerifyPermissionLevel]

    # 로그인 유저 정보 가져오기
    def get(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user)
        # serialized_user_data = UserSerializer(user_profile, many=True).data
        serialized_user_data = UserProfileSerializer(user_profile, many=True).data
        # print("user_profile:", serialized_user_data )
        return Response(serialized_user_data)




# class UserInfoView(APIView):
# permission_classes = [VerifyPermissionLevel]
#
# def get(self, request):
#     user = request.user
#     serialized_user_data = UserSerializer(user).data
#     return Response(serialized_user_data, status=status.HTTP_200_OK)


