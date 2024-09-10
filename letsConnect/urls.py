"""letsConnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path("", include("weconnect.urls")),
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name="weconnect/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="weconnect/logout.html"), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',email_template_name='registration/password_reset_email.html',subject_template_name='registration/password_reset_email.txt',success_url='/accounts/password_reset_done/',from_email='klauspeace95@gmail.com')),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',success_url='/accounts/password_reset_confirm/'), name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html')),

]
