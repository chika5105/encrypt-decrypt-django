from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('ciphers/', views.encrypt_decrypt, name = 'ciphers'),
    path('contact-me/', views.contact_me, name = 'contact-me'),
    path('about/', views.AboutListView.as_view(), name = 'about'),
    path('about/<int:pk>', views.AboutEncryptionView.as_view(), name = 'encryption-detail'),
    path('signup/', views.sign_up, name = 'signup'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user-detail'),

]
#urlpatterns+= [
    #path('accounts/', include ('django.contrib.auth.urls')),
#]