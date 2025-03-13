# Задание 1

from datetime import datetime
import requests

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper


@measure_execution_time
def get_response(url):
    return requests.get(url)

print(get_response('https://www.anekdot.ru/'))



# Задание 2

def requires_admin(func):
    def wrapper(user, username_to_delete):
        if user.get('role') == 'admin':
            return func(user, username_to_delete)
        else:
            raise PermissionError
    return wrapper


@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."


# Пример юзеров
admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}

# Вызовы функции
print(delete_user(admin_user, 'Charlie')) # Должно отработать
print(delete_user(regular_user, 'Charlie')) # Должно рейзить PermissionError