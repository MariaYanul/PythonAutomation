from typing import Callable
from datetime import datetime

row = range(1, 1000)

def decor(function: Callable):
    def decoratee():
        start_time = datetime.now()
        function()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
    return decoratee

@decor
def nums():
    for item in row:
        print(item**2)
    return

nums()