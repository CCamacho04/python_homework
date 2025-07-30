#Task 1
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        msg = (f"function: {func.__name__}"
               f"positional parameters: {args if args else 'none'}"
               f"keyword parameters: {kwargs if kwargs else 'none'}"
               f"return: {result}")
        
        logger.log(logging.INFO, msg)

        return result
    
    return wrapper

@logger_decorator
def hello():
    print("Hello", "World!")

@logger_decorator
def take_pos_arg(*args):
    return True

@logger_decorator
def take_key_arg(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello()
    take_pos_arg(1, 2, 3)
    take_key_arg(x = 8, y = 21)