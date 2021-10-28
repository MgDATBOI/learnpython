print("--- SECTION ONE ---\n")


# This is a normal function
def foo():
    print('[Foo] Ran foo')


foo()
print(f'[Name] Foo name: {foo.__name__}')
# Because a function is an object, it can be use in a variable
bar = foo

bar()

# but bar is just foo in disguise
print(f'[Name] Bar name: {bar.__name__}')


# This is a function with a parameter
def baz(msg):
    print(f'[baz]: {msg}')


baz('Hello')
print(f'[Name] Baz name: {baz.__name__}')

hi = baz
hi('Hi')
print(f'[Name] Hi name: {hi.__name__}')

print("\n--- SECTION TWO ---\n")


# you can use funcitons inside of functions
def add(x, y):
    return x + y


def add_two_numbers(x, y):
    return add(x, y)


# This function takes in two parameters, defines the function _add which prints x + y then returns _add
def add_two_numbers_together(x, y):
    def _add():
        print(x + y)

    return _add


# you can customize functions with the prevous code
add_1_3 = add_two_numbers_together(1, 3)
add_1_3()

add_10_4 = add_two_numbers_together(10, 4)
add_10_4()

print("\n--- SECTION THREE ---\n")


# define Decorator
def outer(func):
    def wrapper(*args, **kwargs):
        print(f'ran {func.__name__} with args: {args} and kwargs: {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def hello_world(a: bool):
    if a:
        print("Hello world")
    else:
        print("Goodbye world")


# this is a Decorator
# You can add code to an existing function
decorated_hw = outer(hello_world)

decorated_hw(True)


@outer
def my_print(*a):
    print(a)


my_print('hi', 'world')


# define a log decorator
def log(func):
    def wrapper(*args, **kwargs):
        print(f'[LOG]: ran {func.__name__}')
        return func(*args, **kwargs)

    return wrapper


# set log mode to on
log_mode = 1


# here is a simple function that takes in msg and returns it in all caps form
def to_caps(msg):
    try:
        return msg.upper()
    except Exception as ex:
        return f"[ERROR]: {ex}"


# if log mode is True, or on, the function will be decorated
if log_mode:
    to_caps = log(to_caps)

print(to_caps("lmaolmaolmao"))

print("\n--- SECTION FOUR ---\n")


# lets take this decorator again
def debug_2(func):
    def wrapper(*args, **kwargs):
        print(f'ran {func.__name__} with args: {args} and kwargs: {kwargs}')
        return func(*args, **kwargs)

    return wrapper


# we can modify a built-in python function to give us more control over it
open = debug_2(open)

with open("test.txt", "w", encoding='utf-8') as f:
    pass
f.close()

print("\n--- SECTION FIVE ---\n")

import time
from colorama import Fore, init

init()


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        now = time.time()
        total_time = now - before
        print(f"{Fore.CYAN}[TIMER]{Fore.RESET} Ran {func.__name__} in {total_time}s")
        return val

    return wrapper


@timer
def wait_3s():
    print('started')
    time.sleep(3)
    print('ended')


wait_3s()
