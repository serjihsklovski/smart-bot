import telebot as tb
import datetime as dt


class Handler:
    def __init__(self, bot_token):
        self._bot = tb.TeleBot(bot_token)

    def run(self):
        @self._bot.message_handler(content_types=['text'])
        def handle_text(sender):
            print('new msg:')
            print('* text: {}'.format(repr(sender.text)))
            print('* from: ' + 'id' + str(sender.chat.id) +
                  (' (@' + sender.chat.username + ')' if sender.chat.username is not None else ''))
            print('* time: ' + str(dt.datetime.fromtimestamp(sender.date)))
            print('-' * 24)

        self._bot.polling(none_stop=True)
