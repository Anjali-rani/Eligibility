from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


app_name= 'accounts'

urlpatterns = [
    url(r'Studentlogin/$', auth_views.LoginView.as_view(template_name='accounts/Studentlogin.html'), name='Studentlogin'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^adminsignup/$', views.admin_signup_view),
    url(r'^adminlogin/$', LoginView.as_view(template_name='accounts/adminlogin.html')),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

]

