import config
from src import app

if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT, host=config.HOST)
