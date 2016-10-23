import mysql.connector as mc
import configparser as cnf
from pathlib import Path
from components.exceptions.config_file_exception import ConfigFileException


class Model:
    def __init__(self, table_name):
        path = Path('config.ini')

        if path.is_file():
            config = cnf.ConfigParser()
            config.read_file(open('config.ini'))

            if 'login' not in config:
                raise ConfigFileException

            for option in ['host', 'database', 'user', 'password']:
                if option not in config['login']:
                    raise ConfigFileException

                else:
                    setattr(self, '_' + option, config['login'][option])

            try:
                self._conn = mc.connect(self._host,
                                        self._database,
                                        self._user,
                                        self._password)

            except mc.Error as err:
                print('smart-bot: "FAILED - {}"'.format(err))

        else:
            raise ConfigFileException

        self._table_name = table_name
