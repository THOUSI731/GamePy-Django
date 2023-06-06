# Django
from django.urls import path

# Local Django
from . import views


urlpatterns = [
    path('signup/',views.signUpPage,name='signUpPage'),
    path('login/',views.logInPage,name='loginPage'),
    path('logout/',views.logOutPage,name="logout"),
    path('',views.dashboard,name='dashboard'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetPassword_validate/<uidb64>/<token>/',views.resetPassword_validate,name='resetPassword_validate'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('my_orders/',views.my_orders,name='my_orders'),
]


