def create_database(cursor, new_database_name):
    """
    creates a new database in mysql

    :param cursor: mysql.connector.connection.cursor object
    :param new_database_name: string
    :return: None
    """
    query = """
        CREATE DATABASE `{}` DEFAULT CHARACTER SET 'utf8'
        """.format(new_database_name)

    cursor.execute(query)
