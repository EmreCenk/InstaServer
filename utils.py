
from Instagram_Automation_Bot.Instagram_Bot_Class import instabot
from Instagram_Automation_Bot.info import bot_username, bot_password
from time import sleep
from random import uniform

def check_for_word(bot: instabot, word: str):
    # the bot will search the site for the word variable.
    # I created a wrapper function because "broken_link" isn't very intuitive.
    return bot.broken_link(keyword=word)


def check_if_followed(bot: instabot, username: str):
    """Checks if the person has already been followed. If not, the bot follows the person. If the account is
    immediately followed, returns true. If the request is pending, returns false. """


    # private = bot.isit_private(username)
    #
    # if private:

    bot.follow(username)

    requested_in_page = check_for_word(bot, "requested") #if requested is inside the page, then we
    return not requested_in_page

    # Alternate way to check:
    # message_in_page = check_for_word(bot, "message")
    # return message_in_page



if __name__ == '__main__':
    bot = instabot(bot_username, bot_password)
    bot.signin()
