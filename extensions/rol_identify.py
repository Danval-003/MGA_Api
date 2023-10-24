from flask_login import login_required, current_user
from extensions.unauthorized import unauthorized
from functools import wraps


def only_worker(func):
    @wraps(func)  # Add the wraps decorator to preserve the original function's metadata
    def wrapper(*args, **kwargs):  # Accept the necessary arguments
        rol = current_user.get_rol()
        if rol == 'trabajador':
            return func(*args, **kwargs)  # Call the original function with arguments
        else:
            print(rol)
            return unauthorized()  # Return the unauthorized response

    return wrapper  # Return the wrapper function without calling it


def only_admin(func):
    @wraps(func)  # Add the wraps decorator to preserve the original function's metadata
    def wrapper(*args, **kwargs):  # Accept the necessary arguments
        rol = current_user.get_rol()
        if rol == 'admin':
            return func(*args, **kwargs)  # Call the original function with arguments
        else:
            return unauthorized()  # Return the unauthorized response

    return wrapper  # Return the wrapper function without calling it

