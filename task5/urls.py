from django.urls import path
from . import views

urlpatterns = [
    path('', views.choice_page, name='choice_page'),
    path('sign_up/', views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
    path('login/', views.login_view, name='login'),
]