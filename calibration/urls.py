from django.urls import path
from . import views
from .views import UpdateEpsressoLog, UpdateFilterLog

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("espresso_log", views.espresso_log, name="espresso_log"),
    path("edit_espresso_log/<int:pk>", UpdateEpsressoLog.as_view(), name="edit_espresso_log"),
    path("filter_log", views.filter_log, name="filter_log"),
    path("edit_filter_log/<int:pk>", UpdateFilterLog.as_view(), name="edit_filter_log"),
]