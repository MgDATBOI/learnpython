from __future__ import annotations

# defining functions
def my_func():
    print("this is a function")


def f1():
    return "this is a function"


def print_my_msg(msg):
    print(f"Your message was: {msg}")


# calling functions
print(f1)
print(f1())
my_func()

# best practice (type hinting)

from typing import Optional, Union


def print_my_msg(msg: Union[str, int]) -> None:
    print(f"Your message was: {msg}")


# def print_my_msg(msg: str | int | float) -> None:
#     print(f"Your message was: {msg}")


