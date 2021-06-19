from Instagram_Automation_Bot.Instagram_Bot_Class import instabot
import utils
import databse_interaction as dbinter

class Server:

    def __init__(self, username, password):
        self.bot = instabot(username, password)

    def check_if_stats_accesible(self, username):
        return utils.check_if_followed(self.bot, username)


    # def go_through_pending_username_list(self, path_to_file):
    #     username_list = dbinter.parse_usernames(path_to_file)
    #     for i in range(len(username_list)):
    #         current_Username = username_list[i]
    #

    def check_username(self, username):
        we_can_access = self.check_if_stats_accesible(username)
        if not we_can_access:
            return False

        followers = self.bot.getstat(username, followersorfollowing="followers")





