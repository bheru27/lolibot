
import sopel.module
import random
from imgurpython import ImgurClient
error = 'sry no workerino'


def albumToImage(album):

    client_id = 'ayy'
    client_secret = 'lmao'
    client = ImgurClient(client_id, client_secret)

    lolisAlbum = client.get_album_images(album)
    loliList = []
    for loli in lolisAlbum:
        loliList.append(loli.link)

    chosenLoli = random.choice(loliList)
    return chosenLoli


@sopel.module.commands('ml')
def mangaList(bot, trigger):
    if trigger.group(2) is None:
        bot.say(error)
    else:
        bot.say('http://myanimelist.net/mangalist/' + trigger.group(2))


@sopel.module.commands('al')
def animeList(bot, trigger):
    if trigger.group(2) is None:
        bot.say(error)
    else:
        bot.say('http://myanimelist.net/animelist/' + trigger.group(2))


@sopel.module.commands('profile')
def mal(bot, trigger):
    if trigger.group(2) is None:
        bot.say(error)
    else:
        bot.say('http://myanimelist.net/profile/' + trigger.group(2))


@sopel.module.commands('lolibot')
def loliBot(bot, trigger):
    bot.msg(trigger.nick, '.ml, .al, .profile, .eyebleach')


@sopel.module.commands('eyebleach')
def eyebleach(bot, trigger):
    bot.say(albumToImage('5fe3N'))


@sopel.module.commands('feelsbleach')
def feelsbleach(bot, trigger):
    bot.say(albumToImage('5fe3N'))


@sopel.module.commands('meme')
def meme(bot, trigger):
    bot.notice('fuck you', trigger.nick)


@sopel.module.commands('list')
def list(bot, trigger):
    bot.notice(
        'What the desu did you just fucking desu about me, you little desu?',
        trigger.nick)
