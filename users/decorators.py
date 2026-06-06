from django.core.exceptions import PermissionDenied
from functools import wraps

def employer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'employer':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def job_seeker_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'job_seeker':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
