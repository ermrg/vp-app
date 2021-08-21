from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from vp import settings


class RoleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user
        if 'setting/' in request.path:
            if user.groups.filter(name='superadmin').exists():
                return None
            return redirect('dashboard')
        return None
