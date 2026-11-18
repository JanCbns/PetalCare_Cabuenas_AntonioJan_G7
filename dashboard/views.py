from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.mixins import RoleRequiredMixin
from accounts.models import CustomUser

Role = CustomUser.Role


@login_required
def dashboard_redirect(request):
    if request.user.role == Role.ADMIN:
        return redirect("admin_dashboard")
    return redirect("owner_dashboard")


class OwnerDashboardView(RoleRequiredMixin, TemplateView):
    allowed_roles = (Role.PLANT_OWNER,)
    template_name = "dashboard/owner_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(total_plants=0, due_today=0, overdue=0, upcoming=[])
        return ctx


class AdminDashboardView(RoleRequiredMixin, TemplateView):
    allowed_roles = (Role.ADMIN,)
    template_name = "dashboard/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_users"] = CustomUser.objects.count()
        ctx["owner_count"] = CustomUser.objects.filter(role=Role.PLANT_OWNER).count()
        ctx["admin_count"] = CustomUser.objects.filter(role=Role.ADMIN).count()
        ctx["recent_users"] = CustomUser.objects.order_by("-date_joined")[:5]
        return ctx