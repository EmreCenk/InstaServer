from Instagram_Automation_Bot.Instagram_Bot_Class import instabot
import utils
import databse_interaction as dbi
from time import sleep
class Server:

    def __init__(self, username, password, headless = False):
        self.bot = instabot(username, password, headless = headless)
        self.bot.signin()

    def check_if_stats_accesible(self, username):
        return utils.check_if_followed(self.bot, username)


    def maintain_users(self, path_to_file, sleep_between_users = 0):
        username_list = dbi.parse_usernames(path_to_file)

        for i in range(len(username_list)):
            unfollowed_people = self.find_who_has_unfollowed(username_list[i])

            if unfollowed_people == False:
                #we could not access the persons data
                print(f"Could not access the data for the user: {username_list[i]} \n")
                sleep(sleep_between_users)

                continue

            print(f"For the user: {username_list[i]}, these people have unfollowed:")
            for u in unfollowed_people:
                print(u)

            print("\n")

            sleep(sleep_between_users)



    def find_who_has_unfollowed(self, username):
        we_can_access = self.check_if_stats_accesible(username)
        if not we_can_access:
            return False


        # Converting both of them to sets reduce the time complexity to O(n) instead of O(n^2)
        # (since lookup times for sets are O(1))
        old_followers = set(dbi.get_followers(username))
        if len(old_followers) == 0:
            #The person is not registered in the database yet.

            dbi.update_followers(username, self.bot.getstat(username, "followers"))
            return [] #there is no way to know who the previous followers were, so we just return nothing

        new_followers = set(self.bot.getstat(username, followersorfollowing="followers"))

        unfollowed_people = set()
        for person in old_followers:
            if person not in new_followers:
                unfollowed_people.add(person)


        #updating the followers in the database:

        dbi.update_followers(username, new_followers)
        return unfollowed_people

    def start_server(self, sleep_time = 10):
        while True:
            self.maintain_users("usernames_to_check", sleep_between_users=sleep_time)


if __name__ == '__main__':
    from Instagram_Automation_Bot.info import username, password
    self = Server(username, password)
    self.start_server(20)
