from django.shortcuts import redirect

def decorator(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('dashboard:login')
        return view_func(request, *args, **kwargs)
    return wrapper