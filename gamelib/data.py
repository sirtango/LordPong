
import os.path

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA = os.path.join(ROOT, 'data')

def scenefile(scenename, filename):
    return os.path.join(os.path.join(DATA, scenename), filename)

def datafile(filename):
    return os.path.join(DATA, filename)
