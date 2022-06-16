from django.db import models

from app import settings


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    # User모델(auth.User를 말한다)은 언제든 변경될 수 있으므로 settings.AUTH_USER_MODEL로 지정하여 좀 더 콘크리트하게 정할 수 있다.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="작성자", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    # category_set에 blank=Ture가 들어가는 이유 : Category가 하나도 지정되지 않았을시에 유효성검사를 실패하기 때문에 blank=True를 작성한다.
    category_set = models.ManyToManyField(Category, blank=True)
    writing = models.TextField()
    is_public = models.BooleanField(default=True, verbose_name="공개 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
