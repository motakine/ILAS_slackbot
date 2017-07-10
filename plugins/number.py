import slackbot.bot
import random

answer = random.randint(1, 50)
max = 50

def number(num):
    '''number 判定
    Args:
        num (int): 判定する数字
    Returns:
        str: num が answer より大きい: 'Too large'
            num が answer より小さい: 'Too small'
            num が answer と一致: 'Correct!'、新しくゲームを始める
            その他: 'Can I kick you?.'
            0は不可思議な数である
            maxが1の時に2以上を答えると1だけだと言われる
    '''
    global answer
    global max

    # 入力された値に応じて返答を構成、正解ならニューゲーム
    if num == 0:
        return ' is a mysterious number...'
    elif num < max + 1:
        if num > answer:
            return ' is too large. The answer is more small.'
        elif num < answer:
            return ' is too small. The answer is more large.'
        elif num == answer:
            answer = random.randint(1, max)
            return ' is correct! :tada: Now, start a new game.'
    elif max == 1:
        return '? Can I kick you? Only 1.'
    return '? Can I kick you? 1 to %d.' % max

def number_set(num):
    '''number set判定
    Args:
        num (int): 判定する数字
    Returns:
        str: 答えのmax（答えになりうる値の最大）を変更する。デフォは50
            1にするとマジ？と訊かれる。それだけ。
            不可思議な数字は0である
    '''
    global answer
    global max

    # 入力された値に応じて返答を構成、maxを変更、ニューゲーム
    if num == 0:
        return 'There is a mysterious number... It is '
    elif num == 1:
        max = 1
        answer = random.randint(1, max)
        return '1? Really? Then, the maximum of the answer is '
    max = num
    answer = random.randint(1, max)
    return 'OK. Then, the maximum of the answer is '

@slackbot.bot.respond_to(r'^number\s+set\s+(\d+)')
def resp_set(message, digitstr):
    '''number set (数字) 形式への返答
    （数字）部のnumber set判定を行い、返事する
    Args:
    '''
    # number set 判定
    nbs = number_set(int(digitstr))

    # 返事する文字列を構成
    reply = '{0:s}{1:s}.'.format(nbs, digitstr)

    message.reply(reply)

@slackbot.bot.respond_to(r'^number\s+(\d+)')
def resp_number(message, digitstr):
    '''number (数字) 形式への返答
    (数字) 部のnumber判定を行い, 'number (数字) 判定' を返事する
    Args:
        message (slackbot.dispatcher.Message): slack message
        digtstr (str): 数値の文字列
    '''

    # number 判定
    nb = number(int(digitstr))

    # 返事する文字列を構成
    reply = '{0:s}{1:s}'.format(digitstr, nb)

    message.reply(reply)

@slackbot.bot.respond_to(r'^number\s+giveup')
def resp_giveup(message):
    '''number giveup への返答
    正解を表示し、新しい正解を設定、'Start a new game.'を返す
    Args:
        
    '''
    global answer
    global max

    # 表示する答えを設定、次のゲームの解答を設定
    showanswer = answer
    answer = random.randint(1, max)

    # 返事する文字列を構成
    message.reply('Hahaha! Failed! :ghost: The answer is %d. Start a new game.' % showanswer)
    message.react('stuck_out_tongue_winking_eye')
    
