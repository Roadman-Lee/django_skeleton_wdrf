from django.urls import path

from blog.views import ArticleApiView

urlpatterns = [
    path('', ArticleApiView.as_view())
]
