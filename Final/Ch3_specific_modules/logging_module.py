import logging

# basics

LOG_FORMAT = "%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
#
# logging.basicConfig(filename="../logs/log.log", level=logging.INFO, format=LOG_FORMAT)

# https://docs.python.org/3/library/logging.html#logrecord-attributes

# DEBUG:      Detailed information, typically of interest only when diagnosing problems.
#
# INFO:       Confirmation that things are working as expected.
#
# WARNING:    An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
#
# ERROR:      Due to a more serious problem, the software has not been able to perform some function.
#
# CRITICAL:   A serious error, indicating that the program itself may be unable to continue running.


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


num_1 = 10
num_2 = 5

# add_result = add(num_1, num_2)
# print(f"Add: {num_1} + {num_2} = {add_result}")
# logging.info(f"Add: {num_1} + {num_2} = {add_result}")
#
# sub_result = add(num_1, num_2)
# print(f"Sub: {num_1} - {num_2} = {sub_result}")
# logging.info(f"Sub: {num_1} - {num_2} = {sub_result}")


# advanced

print(__file__)
print(__file__.split("\\")[-1])
print(__name__)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(LOG_FORMAT)

file_handler = logging.FileHandler("../logs/log.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


add_result = add(num_1, num_2)
print(f"Add: {num_1} + {num_2} = {add_result}")
logger.info(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = add(num_1, num_2)
print(f"Sub: {num_1} - {num_2} = {sub_result}")
logger.info(f"Sub: {num_1} - {num_2} = {sub_result}")

# logging.exception()
