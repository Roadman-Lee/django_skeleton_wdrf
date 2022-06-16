from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from rest_framework import permissions, status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from blog.serializers import ArticleSerializer, AuthorSerializer


class RegistedMoreThanSomeDaysUser(BasePermission):
    """
    가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """

    message = "가입 후 1주일 이상 지난 사용자만 사용하실 수 있습니다."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.join_date < (timezone.now() - timedelta(days=3))
        )


class ArticleApiView(APIView):
    # permission_classes = [RegistedMoreThanSomeDaysUser]
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    # 모든 글 리스트 업
    def get(self, request):
        user = request.user
        article = Article.objects.filter(author=user)
        serialized_article_data = ArticleSerializer(article, many=True).data
        return Response(serialized_article_data)

    # 글 생성
    def post(self, request):
        print("데이터 : ", request.user)
        user = request.user
        serializer = ArticleSerializer(data=request.data, instance=user)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


