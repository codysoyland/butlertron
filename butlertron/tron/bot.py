from ircbot import SingleServerIRCBot
from irclib import nm_to_n
from tron.exceptions import NoRoutes
from tron.dispatcher import Dispatcher
from tron.message import Message
import routes

class Client(SingleServerIRCBot):
    def __init__(self, channel, nick, server, port=6667):
        SingleServerIRCBot.__init__(self, [(server, port)], nick, nick)
        self.channel = '#' + channel

    def on_nicknameinuse(self, connection, event):
        connection.nick(connection.get_nickname() + "_")

class Bot(object):
    def __init__(self, settings):
        self.settings = settings
        self.client = Client(
            channel = settings.CHANNEL,
            nick = settings.NICK,
            server = settings.SERVER,
            port = settings.PORT,
        )
        self.connection = self.client.connection
        self.channel = '#' + settings.CHANNEL
        self.register_callbacks()

    def start(self):
        self.client.start()

    def register_callbacks(self):
        for method_name in dir(self):
            method = getattr(self, method_name)
            if hasattr(method, 'handler'):
                self.connection.add_global_handler(method.handler, method)

    def add_handler(type):
        def decorator(callback):
            callback.handler = type
            return callback
        return decorator

    @add_handler('welcome')
    def join(self, connection, event):
        connection.join(self.channel)

    # would be nice to have support for multiple decorators.
    # should be simple to add.
    #@add_handler('privmsg')
    @add_handler('pubmsg')
    def dispatch(self, connection, event):
        message = Message(
            message = event.arguments()[0],
            nick = nm_to_n(event.source()),
            event = event,
            connection = self.connection,
            bot = self
        )
        dispatcher = Dispatcher(routes.routes)
        try:
            responder, arguments = dispatcher.resolve(message.message)
        except NoRoutes:
            if self.settings.DEBUG:
                print 'No route detected for message "%s"' % message.message
        else:
            responder(message, **arguments)

    def say(self, message):
        self.connection.privmsg(self.channel, message)

    def reply(self, event, message):
        if event.target() == self.channel:
            target = self.channel
        else:
            target = event.source().split('!')[0]
        self.connection.privmsg(target, message)

