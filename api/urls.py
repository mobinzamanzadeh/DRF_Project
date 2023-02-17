from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', ArticleViewSet)
router.register('users', UserViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]

# urlpatterns = [
#     # path("", ArticleList.as_view(), name="list"),
#     # path("<int:pk>", ArticleDetail.as_view(), name="detail"),
#     # path("users/", UserList.as_view(), name="user-list"),
#     # path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
# ]