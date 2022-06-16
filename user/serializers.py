from rest_framework import serializers

from blog.models import Article
from user.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = UserArticleSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "join_date",
            "userprofile",
            "article_set",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password", "join_date")
        extra_kwargs = {
            "password": {"write_only": True},
        }
