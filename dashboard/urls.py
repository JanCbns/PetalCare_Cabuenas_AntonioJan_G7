from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_redirect, name="dashboard"),
    path("owner/", views.OwnerDashboardView.as_view(), name="owner_dashboard"),
    path("admin-dashboard/", views.AdminDashboardView.as_view(), name="admin_dashboard"),
]