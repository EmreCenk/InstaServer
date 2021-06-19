from Instagram_Automation_Bot.Instagram_Bot_Class import instabot
import utils
import databse_interaction as dbi

class Server:

    def __init__(self, username, password):
        self.bot = instabot(username, password)

    def check_if_stats_accesible(self, username):
        return utils.check_if_followed(self.bot, username)


    # def go_through_pending_username_list(self, path_to_file):
    #     username_list = dbi.parse_usernames(path_to_file)
    #     for i in range(len(username_list)):
    #         current_Username = username_list[i]
    #

    def get_unfollowed_and_update_database(self, username):
        we_can_access = self.check_if_stats_accesible(username)
        if not we_can_access:
            return False


        # Converting both of them to sets reduce the time complexity to O(n) instead of O(n^2)
        # (since lookup times for sets are O(1))
        old_followers = set(dbi.get_followers(username))
        new_followers = set(self.bot.getstat(username, followersorfollowing="followers"))

        unfollowed_people = set()
        for person in old_followers:
            if person not in new_followers:
                unfollowed_people.add(person)


        #updating the followers in the database:

        dbi.update_followers(username, new_followers)

        return unfollowed_people

