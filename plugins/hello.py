import slackbot.bot

@slackbot.bot.listen_to('hello')
def resp_hello(message):
    message.reply('こんにちは')

@slackbot.bot.respond_to('hello')
def resp_hello(message):
    message.reply('こんにちは')

@slackbot.bot.respond_to('bye')
def resp_hello(message):
    message.reply('fuck')

@slackbot.bot.respond_to('bubble')
def resp_hello(message):
    message.reply('ぶくぶく')