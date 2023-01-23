import subprocess
import json

def pip_freeze(event):
    result = subprocess.run(['pip freeze'], stdout=subprocess.PIPE, shell=True)
    stdout = result.stdout.decode('utf-8')
    packages = stdout.split('\n')
    print(f'Hi event: {event}')
    print(f'Hi locals: {packages}')
    return {'packages': packages}


def mul(n):
    return n * 2


# echo class, custom class example
class Echo:
    def __init__(self, context, name=None, **kw):
        self.context = context
        self.name = name
        self.kw = kw

    def do(self, x='no tov'):
        print("Echo:", self.name, x)
        return x