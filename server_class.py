from Instagram_Automation_Bot.Instagram_Bot_Class import instabot
from utils import check_for_word, check_if_followed
class Server:

    def __init__(self, username, password):
        self.bot = instabot(username, password)

    def check_if_followed(self, username):
        return check_if_followed(self.bot, username)


    
