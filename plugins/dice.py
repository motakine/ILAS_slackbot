import slackbot.bot
import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

@slackbot.bot.respond_to('dice')
def resp_dice(message):
    message.reply(dice1, dice2)
