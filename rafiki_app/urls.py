from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('employer/', views.employer, name='employer'),
    path('employee/', views.employee, name='employee'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('profile/<str:username>/', views.public_profile, name='public-profile'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)