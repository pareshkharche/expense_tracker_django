
from django.urls import path
from tracker.views import index, deleteTransaction, registration, login_page, logout_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('registration/', registration , name="registration"),
    path('login/', login_page , name="login_page"),
    path('logout/', logout_page , name="logout_page"),
    path('delete-tranaction/<uuid>', deleteTransaction, name="deleteTransaction"),
    
    
     # Other URL patterns
    path('password-reset/', auth_views.PasswordResetView.as_view(
    template_name='password_reset.html'), name='password_reset'),
path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='password_reset_done.html'), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='password_reset_confirm.html'), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
    template_name='password_reset_complete.html'), name='password_reset_complete'),

   

]
