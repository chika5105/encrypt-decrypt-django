from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('ciphers/', views.encrypt_decrypt, name = 'ciphers'),
    path('contact-me/', views.contact_me, name = 'contact-me'),
    path('about/', cache_page(60 * 15)(views.AboutListView.as_view()), name = 'about'),
    path('about/<int:pk>', cache_page(60 * 15)(views.AboutEncryptionView.as_view()), name = 'encryption-detail'),
    path('signup/', views.sign_up, name = 'signup'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),
    path('user-delete-success', views.user_delete_success, name = 'user-delete-success'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('user-update-success', views.user_update_success, name = 'user-update-success'),
    path('cipher-game/', cache_page(60 * 15)(views.CipherGameListView.as_view()), name = 'cipher-game'),
    path('cipher-game/<int:pk>/', views.solve_game, name = 'cipher-game-detail'),
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('instructions/', views.instructions, name = 'instructions')



]
#urlpatterns+= [
    #path('accounts/', include ('django.contrib.auth.urls')),
#]