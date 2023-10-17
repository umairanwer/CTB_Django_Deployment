from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name='logout'),
    path('delete/', views.DeleteView, name='delete'),
    path('verify_email/<str:token>', views.verify_email_view, name='verify_email_view')
]
