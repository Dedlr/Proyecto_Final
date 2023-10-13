from django.contrib import admin
from django.urls import path,include

from apps.users.views.views_user import Login,Logout

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('login/',Login.as_view(),name='Login'),
    path('logout/',Logout.as_view(),name='Logout'),
    path('admin/', admin.site.urls),
    path('user/',include('apps.users.router')),
 

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]