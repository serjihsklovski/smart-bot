"""
by running this file you create a new smart-bot database in your mysql.
all you have to do is input your mysql username, password and token of your bot.
"""
import mysql.connector as mc
import telebot as tb
from components import create_database
from components import drop_database

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
                    'smart-bot: "OK - database for @{0} was created. ' +
                    'it is called `{1}`"'
                ).format(bot_info.username, smart_bot_database_name)
            )

            conn.database = smart_bot_database_name

            tables = {
                'info':
                    'CREATE TABLE `info` (' +
                    '`name` varchar(128) NOT NULL UNIQUE, ' +
                    '`value` varchar(255) DEFAULT NULL' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'command':
                    'CREATE TABLE `command` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`name` varchar(255) NOT NULL UNIQUE, ' +
                    '`description` text' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'status':
                    'CREATE TABLE `status` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`name` varchar(128) NOT NULL UNIQUE, ' +
                    '`description` text' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'language':
                    'CREATE TABLE `language` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`name` varchar(12) NOT NULL UNIQUE' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'contact':
                    'CREATE TABLE `contact` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`telegram_id` int(11) NOT NULL UNIQUE, ' +
                    '`username` varchar(255) DEFAULT NULL, ' +
                    '`first_name` varchar(255) DEFAULT NULL, ' +
                    '`last_name` varchar(255) DEFAULT NULL, ' +
                    '`rating` int(11) NOT NULL, ' +
                    '`status_id` int(11) DEFAULT NULL, ' +
                    '`language_id` int(11) DEFAULT NULL' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'mention':
                    'CREATE TABLE `mention` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`value`  varchar(255) NOT NULL UNIQUE, ' +
                    '`description` text' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8',

                'replica':
                    'CREATE TABLE `replica` (' +
                    '`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, ' +
                    '`value` text, ' +
                    '`mention_id` int(11) DEFAULT NULL, ' +
                    '`language_id` int(11) DEFAULT NULL' +
                    ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
            }

            for k in tables:
                try:
                    print('smart-bot: "creating table `{0}`.`{1}`"'.format(
                        smart_bot_database_name, k
                    ))

                    curs.execute(tables[k])

                except mc.Error as err:
                    print('smart-bot: "FAILED - {}"'.format(err))
                    drop_database(curs, smart_bot_database_name)
                    print('smart-bot: "init - cancelled"')
                    break

            else:
                print('smart-bot: "OK - all tables were created successfully"')

        finally:
            curs.close()

    finally:
        conn.close()
