"""
by running this file you create a new smart-bot database in your mysql.
all you have to do is input your mysql username, password and token of your bot.
"""
import mysql.connector as mc
import telebot as tb
from components import create_database

print('smart-bot: "input your mysql username"')
username = input('you: ')
print('smart-bot: "input your mysql password"')
password = input('you: ')

login = {
    'host': '127.0.0.1',
    'database': 'mysql',
    'user': username,
    'password': password
}

try:
    conn = mc.connect(**login)

except mc.Error as err:
    print('smart-bot: "FAILED - {}"'.format(err))
    exit(1)

else:
    print('smart-bot: "OK - the connection is established"')
    print('smart-bot: "input the token of your bot"')
    token = input('you: ')

    try:
        bot = tb.TeleBot(token)
        bot_info = bot.get_me()

        smart_bot_database_name = 'smart_bot_' + bot_info.username

    except tb.apihelper.ApiException as exc:
        print('smart-bot: "FAILED - {}"'.format(exc))
        exit(1)

    else:
        curs = conn.cursor()

        try:
            create_database(curs, smart_bot_database_name)

        except mc.Error as err:
            print('smart-bot: "FAILED - {}"'.format(err))

        else:
            print(
                (
                    'smart-bot: "OK - database for {0} was created. ' +
                    'it is called `{1}`"'
                ).format(bot_info.username, smart_bot_database_name)
            )

            # create tables here

        finally:
            curs.close()

    finally:
        conn.close()
