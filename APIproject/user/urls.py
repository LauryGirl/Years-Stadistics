from django.urls import include, path
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register(r'roles', views.RoleViewSet, basename='roles')
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'admins', views.AdminUserViewSet, basename='admins')


urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.ProfileView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('login/admin/', views.AdminLoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('code/verify/', views.VerifyCodeView.as_view()),
    path('password/change/', views.ChangePasswordView.as_view()),
    path('recoverpassword/change/', views.ChangeRecoverPasswordView.as_view()),
    path('password/restore/', views.RestorePasswordView.as_view()),
    path('password/recover/', views.RecoverPasswordView.as_view()),
    path('code/send/', views.SendCodeView.as_view()),
    path('token/', views.TokenView.as_view()),
    path('token/validate/', views.TokenValidatorView.as_view())
]
