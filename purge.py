"""
by running this file you delete old smart-bot database and after that you can
set a new bot and create a database for it.
"""
import configparser as cnf
import mysql.connector as mc
from pathlib import Path
from components.exceptions.config_file_exception import ConfigFileException
from components import drop_database
from os import remove

path = Path('config.ini')

if path.is_file():
    config = cnf.ConfigParser()
    config.read_file(open(path.name))

    if 'login' not in config:
        raise ConfigFileException

    for option in ['host', 'database', 'user', 'password']:
        if option not in config['login']:
            raise ConfigFileException('smart-bot: "option `{option}` does not '
                                      'exist"'.format(option=option))

    else:
        try:
            conn = mc.connect(host=config['login']['host'],
                              user=config['login']['user'],
                              password=config['login']['password'])

            curs = conn.cursor()

            drop_database(curs, config['login']['database'])

            print('smart-bot: "OK - database `{}` was deleted"'.format(
                config['login']['database']
            ))

            curs.close()
            conn.close()

        except mc.Error as err:
            print('smart-bot: "FAILED - {}"'.format(err))

        else:
            remove(path.name)

else:
    print('smart-bot: "FAILED - file `config.ini` is not found!"')
