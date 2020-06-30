"""LITS_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from application import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


handler404 = 'application.views.error_404'
handler500 = 'application.views.error_500'

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PayrollAttendanceIndexPage.as_view(), name="index"),
    path('employee/index/', views.PayrallAttendanceEmployeeIndexPage.as_view(), name="employee_index"),
    
    # Update password    
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Password reset
    path('accounts/password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Login and register
    path('login/', views.login_page, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register_page, name="register"), 

    path('application/', include('application.urls')),

    # path('error500/', views.error_500, name="error500"), 
    # path('error404/', views.error_404, name="error404"), 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


