from django.shortcuts import render, redirect

# Authenticated
def auth(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request, *args, **kwargs)
    return wrapped_view

def guest(view_function):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return redirect('dashboard')
        return view_function(request, *args, **kwargs)
    return wrapped_view