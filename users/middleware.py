from django.shortcuts import redirect

class RoleBasedRedirectMiddleware:
    """
    Optionally enforce role-based redirects for authenticated users
    trying to access unauthorized sections.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Example: Prevent job seekers from accessing employer URLs and vice versa
        if request.user.is_authenticated:
            path = request.path
            if path.startswith('/users/employer') and request.user.role != 'employer':
                return redirect('job_seeker_dashboard')
            if path.startswith('/users/seeker') and request.user.role != 'job_seeker':
                return redirect('employer_dashboard')
        return self.get_response(request)
