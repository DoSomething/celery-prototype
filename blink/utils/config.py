from os import path
import sys

from dotenv import load_dotenv

def load_env():
    app = sys.modules['__main__']
    dotenv_path = path.join(path.dirname(app.__file__), '.env')
    if (path.exists(dotenv_path)): load_dotenv(dotenv_path)
