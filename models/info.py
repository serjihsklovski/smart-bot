from models import Model


class Info(Model):
    def __init__(self):
        Model.__init__(self, self.__class__.__name__.lower())

    def add_id(self, bot_id):
        curs = self._conn.cursor()

        query = 'INSERT INTO `{table}` (`name`, `value`) VALUES (%s, %s)'.format(
            table=self._table_name
        )

        values = ('id', bot_id)

        curs.execute(query, values)
        self._conn.commit()
        curs.close()

    def add_username(self, bot_username):
        curs = self._conn.cursor()

        query = 'INSERT INTO `{table}` (`name`, `value`) VALUES (%s, %s)'.format(
            table=self._table_name
        )

        values = ('username', bot_username)

        curs.execute(query, values)
        self._conn.commit()
        curs.close()

    def add_first_name(self, bot_first_name):
        curs = self._conn.cursor()

        query = 'INSERT INTO `{table}` (`name`, `value`) VALUES (%s, %s)'.format(
            table=self._table_name
        )

        values = ('first_name', bot_first_name)

        curs.execute(query, values)
        self._conn.commit()
        curs.close()

    def add_last_name(self, bot_last_name):
        curs = self._conn.cursor()

        query = 'INSERT INTO `{table}` (`name`, `value`) VALUES (%s, %s)'.format(
            table=self._table_name
        )

        values = ('last_name', bot_last_name)

        curs.execute(query, values)
        self._conn.commit()
        curs.close()

    def add_info(self, bot_info):
        """
        inserts id, username, first_name and last_name into `info` table

        :param bot_info: json-object obtained from TeleBot.get_me method
        :return: None
        """
        self.add_id(bot_info.id)
        self.add_username(bot_info.username)
        self.add_first_name(bot_info.first_name)
        self.add_last_name(bot_info.last_name)
