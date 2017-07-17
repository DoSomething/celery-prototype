from blink.utils.config import load_env
load_env()

from blink.web import app

if __name__ == '__main__':
    app.run()
