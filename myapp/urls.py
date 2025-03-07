from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views



urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("student/", views.StudentView.as_view(), name = "student"),
    path("student/<int:id>/", views.StudentDetailView.as_view(), name = "student_detail"),
    path("classroom/", views.ClassRoomView.as_view(), name = "classroom"),
    path("classroom/<int:id>/", views.ClassRoomView.as_view(), name = "classroom_patch"),
    
]