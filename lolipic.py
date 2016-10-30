#!/usr/bin/env python3
import sopel.module
import random
from imgurpython import ImgurClient

# startup block


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

# Image commands


@sopel.module.commands('myloli')
def myLoli(bot, trigger):
    bot.say('https://i.imgur.com/WomxOdy.png')


@sopel.module.commands('wat')
def wat(bot, trigger):
    bot.say('https://puu.sh/m9pg5/a61e6fd4dd.jpg')


@sopel.module.commands('scum')
def scum(bot, trigger):
    bot.say('https://i.imgur.com/0pXo5WW.gif')

# Album commands


@sopel.module.commands('railgun')
def railgun(bot, trigger):
    bot.say(albumToImage('0LcUd'))


@sopel.module.commands('gahara')
def gahara(bot, trigger):
    bot.say(albumToImage('9ELw2'))


@sopel.module.commands('henneko')
def henneko(bot, trigger):
    bot.say(albumToImage('NW0f1'))


@sopel.module.commands('shinobu')
def shinobu(bot, trigger):
    bot.say(albumToImage('bi6Jl'))


@sopel.module.commands('8kuji')
def hackikuji(bot, trigger):
    bot.say(albumToImage('LbaKB'))


@sopel.module.commands('chiyo')
def chiyoz(bot, trigger):
    bot.say(albumToImage('JioGT'))


@sopel.module.commands('saekano')
def saekano(bot, trigger):
    bot.say(albumToImage('5GIpi'))


@sopel.module.commands('lewd')
def lewd(bot, trigger):
    bot.say(albumToImage('aGToi'))


@sopel.module.commands('neko')
def neko(bot, trigger):
    bot.say(albumToImage('zUIJj'))


@sopel.module.commands('gif')
def gif(bot, trigger):
    bot.say(albumToImage('Y6NQW'))


@sopel.module.commands('8ball')
def hachiball(bot, trigger):
    choices = [
        'Signs point to yes',
        'Yes',
        'Reply hazy, try again',
        'Without a doubt',
        'My sources say no',
        'As I see it, yes',
        'You may rely on it',
        'Concentrate and ask again',
        'Outlook not so good',
        'It is decidedly so',
        'Better not tell you now',
        'Very doubtful',
        'Yes - definitely',
        'It is certain',
        'Cannot predict now',
        'Most likely',
        'Ask again later',
        'My reply is no',
        'Outlook good',
        'Don\'t count on it']
    bot.say(trigger.nick + ': ' + random.choice(choices))


@sopel.module.commands('echo')
def echo(bot, trigger):
    if trigger.nick in ['List admin nicks here']:
        bot.say(trigger.group(2))
    else:
        return False
