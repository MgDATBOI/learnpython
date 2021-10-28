from typing import Optional, Union

# docstrings
def sum(x: Union[int, float] = 0, y: Union[int, float] = 0) -> Union[int, float]:
    """Returns the sum of two numbers.

    Args:
        x: The first parameter that will be added.
        y: The second parameter that will be added.

    Returns:
        The return sum of the two parameters. Int if the first and second parameter are type int else float.
    """
    return x + y


# hover mouse over <sum>
s = sum(1, 3)
print(s)

# examples


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    return str(param1) == param2


function_with_types_in_docstring(1, "2")

print(help(function_with_types_in_docstring))
print(function_with_types_in_docstring.__doc__)
