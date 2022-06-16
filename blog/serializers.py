from rest_framework import serializers

from blog.models import Article
from user.models import User
from user.serializers import UserProfileSerializer


class AuthorSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = "__all__"
