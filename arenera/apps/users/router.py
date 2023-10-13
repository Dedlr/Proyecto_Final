from rest_framework.routers import DefaultRouter

from apps.users.views.views import UserViewSet

router = DefaultRouter()

router.register('', UserViewSet, basename="users")

urlpatterns = router.urls