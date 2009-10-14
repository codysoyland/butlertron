def reply(reply_message):
    def responder(message, **kwargs):
        message.reply(reply_message % kwargs)
    return responder
