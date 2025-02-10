import os
import random
import sys
import time


def generate_random_proxy(proxy_list):
    if proxy_list and len(proxy_list) > 0:
        proxy_string = random.choice(proxy_list)
        proxies = {
            'https': f'http://{proxy_string}',  # must  'https': f'https://{PROXY_STRING}', not f'http
            'http': f'http://{proxy_string}'
        }
    else:
        proxies = {}
    return proxies


def with_retries(max_retries=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = kwargs.pop('user', None)
            for counter in range(max_retries):
                try:
                    response = func(*args, **kwargs)
                    return response
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    err_message = f"{e}. {exc_type, f_name, exc_tb.tb_lineno}"
                    print(f"\t{func.__name__}({args, kwargs})|(user:{user}) Retry Exception (counter={counter}): {err_message}\n")
                    # logger.error(f'(user:{user}) Retry Exception (counter={counter}): {err_message}')
                    time.sleep(0.5)
            return None
        return wrapper
    return decorator
