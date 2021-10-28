# basic type hinting

# def function_name(argument1: type1, argument2: type2) -> returnType:
#     code...

# def function_name(argument1: Optional[type1] = None, argument2: Union[type2, type3] = 0) -> returnType:
#     code...

def f1(arg1: int, arg2: str) -> str:
    return f"[{arg1}] | {arg2}"


print(f1(1, "lmao"))

# from typing import Optional, Union
from typing import Optional, Union

# def function_name(argument1: Optional[type1] = None, argument2: Union[type2, type3] = 0) -> returnType:
#     code...


def f2(arg1: int, arg2: str) -> Optional[str]:
    if isinstance(arg1, int) and isinstance(arg2, str):
        return f"[{arg1}] | {arg2})"
    else:
        # return None
        raise ValueError("arg1 must be type int") if not isinstance(
            arg1, int
        ) else ValueError("arg2 must be type str")


print(f2(2, "lmao"))
# print(f2("3", "lmao"))


def f3(arg1: int, arg2: Optional[str] = None) -> str:
    if arg2 is None:
        return f"[{arg1}]"
    else:
        return f"[{arg1}] | {arg2}"


print(f3(4))
print(f3(5, "lmao"))

# from __future__ import annotations
from __future__ import annotations

def f4(arg1: int, arg2: str | None = None) -> str:
    if arg2 is None:
        return f"[{arg1}]"
    else:
        return f"[{arg1}] | {arg2}"

print(f4(6))
print(f4(7, "lmao"))