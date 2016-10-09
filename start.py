import configparser as cnf
from components.handler import Handler

config = cnf.ConfigParser()
config.read_file(open('config.ini'))

Handler(config['telegram']['bot_token']).run()
