import os

from app import create_app

config_name = os.getenv('APP_SETTING') # config_name = "development"
app =  create_app(config_name)

if __name__ == '__main__':
    app.run()