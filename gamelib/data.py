
import os.path

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA = os.path.join(ROOT, 'data')

def datafile(filename):
    return os.path.join(DATA, filename)
