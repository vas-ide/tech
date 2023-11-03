

from contextlib import contextmanager

@contextmanager
def some_generator(fole_name):
    code = open(fole_name)
    yield code
    code.close()


with some_generator(__file__) as file:
    print(file)


