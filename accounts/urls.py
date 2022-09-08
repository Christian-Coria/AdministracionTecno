from django.urls import path
from.views import PanelLogin, PanelLogout, SignUpView
from accounts.views import perfil , editar_perfil
#from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
    path("signup/", SignUpView.as_view(), name="panel-signup"),
    path("perfil/", perfil, name="perfil"),
    path("editar/perfil/", editar_perfil, name="editar_perfil"),

#     path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
#     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
#     path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
 ]