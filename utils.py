from datetime import datetime
from functools import wraps

def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def wrapper(*args, **kwargs):
            
            result = old_function(*args, **kwargs)
            
            data = {
                'date' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'func_name' : wrapper.__name__,
                'args' : args,
                'kwargs' : kwargs,
                'result' : result
            }
            
            with open(path, 'a', encoding='utf-8') as lf:
                lf.write(f'{data}\n')
            
            return result
        
        return wrapper
    return __logger
