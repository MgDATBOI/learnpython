# https://www.youtube.com/watch?v=0eeweCiUU4U

# print(
#     (
#         lambda expr, stack: all(
#             len(stack) == 0 if char is None else
#             stack.append(char) or True if char in "([{" else # stack.append(char) returns false
#             len(stack) > 0 and {"(": ")", "[": "]", "{": "}"}[stack.pop()] == char if char in ")]}" else
#             True
#             for char in expr 
#         )
#     )(
#         list(input()) + [None], []
#     )
# )

print((lambda expr, stack: all(len(stack) == 0 if char is None else stack.append(char) or True if char in "([{" else len(stack) > 0 and {"(": ")", "[": "]", "{": "}"}[stack.pop()] == char if char in ")]}" else True for char in expr))(list(input()) + [None], []))