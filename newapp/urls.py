from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('posts/', views.multipost, name="posts"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/logout/', views.logout_view, name="logout"),
    path('accounts/profile/history/', views.history, name="history"),
    path('accounts/profile/history/flush/', views.history_flush, name="history_flush"),
    path('register/', views.registerview, name="register"),
    #path('search_results/', views.publicSearch, name="publicSearch"),
]
