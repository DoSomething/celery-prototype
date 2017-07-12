from os import path

from dotenv import load_dotenv

def load_env():
    dotenv_path = path.join(path.dirname(path.abspath(__file__)), '.env')
    if (path.exists(dotenv_path)): load_dotenv(dotenv_path)
