from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('register/', views.register, name='register'),  # Страница регистрации
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Страница входа
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Страница выхода
    path('accounts/profile/', views.profile_view, name='profile'),  # Добавьте маршрут для профиля
    # другие маршруты
]
