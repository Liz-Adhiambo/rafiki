from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),

    path('services/', views.services , name = 'services'),
    path('profile/', views.profile, name= 'profile'),

    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('employer/', views.employer, name='employer'),
    path('employee/', views.employee, name='employee'),



    path('update_profile/', views.update_profile, name='update_profile'),

    path('employee/<str:username>/', views.public_profile, name='public-profile'),
    path('search/', views.search_profile, name = 'search_profile'),
    path('logout/', views.logout, name='logout'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
