from src.some_helpers import mul
from random import randint
import os


def _walk():
    files = [os.path.join(path, name) for path, subdirs, files in os.walk('/') for name in files]
    return list(filter(lambda x: x.startswith('/'), files))


def great(event):
    # print(f'{locals()}')
    print('Greatings ?!')
    # return {'walk': _walk()}
    output = {'name': 'great',
              'walk': _walk(),
              'event': event,
              'output': f'Greatings, before me: {mul(randint(1, 10))}'}
    return output


def handling(event):
    print('handling')
    return {'name': 'handling', 'event': event, 'handle': 'ing', 'inputs': ['list', 'of', 'inputs', 'for', 'model']}



