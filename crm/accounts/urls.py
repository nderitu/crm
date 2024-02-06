from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='dashboard'),
    path('user/', views.user_page, name='user-page'),

    path('account/', views.account_settings, name='account'),

    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),

    path('create_order_customer/<str:pk>', views.create_order_customer, name='create_order_customer'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_complete'),
]

'''
Password Reset Urls/Procedure
1 - Submit email form                      //PasswordResetView.as_view()
2 - Email sent success message             //PasswordResetDoneView.as_view()
3 - Link to password Reset form in email   //PasswordResetConfirmView.as_view()
4 - Password successfully changed message  //PasswordResetCompleteView.as_view()
'''
