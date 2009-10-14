class Message(object):
    def __init__(self, message, nick, event, connection, bot):
        self.message = message
        self.nick = nick
        self.event = event
        self.connection = connection
        self.bot = bot
    def reply(self, message):
        if self.event.target() == self.bot.channel:
            message = '%s: %s' % (self.event.source().split('!')[0], message)
        self.bot.reply(self.event, message)
