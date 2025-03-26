from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from myapp.views import RegisterView, LoginView, DashboardView, ArticleListView, ArticleDetailView, ArticleCreateView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name = 'auth_register'),
    path('api/auth/login/', LoginView.as_view(), name = 'auth_login'),
    path('api/dashboard/', DashboardView.as_view(), name = 'dashboard'),
    path('api/articles/', ArticleListView.as_view(), name = 'article_list'),
    path('api/articles/create/', ArticleCreateView.as_view(), name = 'article_create'),
    path('api/articles/<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),

]