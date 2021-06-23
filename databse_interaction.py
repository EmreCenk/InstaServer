
# for now I will be using a text file to emulate a database. Hopefully I won't need to create an actual remote databse
# in the future.
import os
def parse_usernames(file_path: str, separator_character: str = "\n"):
    file = open(file_path, "r")
    username_list = file.read().split(separator_character)
    file.close()

    return username_list

def remove_line(file_path: str, index: int, separator_character: str = "\n"):
    username_list = parse_usernames(file_path, separator_character)
    file = open(file_path, "w")

    new_text = ""
    try:
        username_list.pop(index)
    except IndexError:
        print("IndexError at the 'remove_line' function in 'databse_inteaction.py'")
        return
    for i in range(len(username_list)):
        new_text += str(username_list[i]) + "\n"

    new_text = new_text[:-1]

    file.write(new_text)
    file.close()

    return new_text

def get_parsed_cwd(parent_directory = "InstaServer"):
    working_directory = os.getcwd().split("\ "[:-1])
    final_dir = ""
    for d in working_directory:
        final_dir += d +"\ "[:-1]
        if d == parent_directory:
            break

    return final_dir[:-1]


def update_followers(username, new_follower_list):

    backslash = r"\ "[:-1]
    file = open(f"{get_parsed_cwd()}\Latest_Followers"+ backslash +f"{username}.txt", "w")
    text = "\n".join(new_follower_list)
    file.write(text)
    file.close()


def get_followers(username):
    backslash = r"\ "[:-1]

    try:
        file = open(f"{get_parsed_cwd()}\Latest_Followers"+ backslash +f"{username}.txt", "r")
    except FileNotFoundError:
        return []

    follower_list = file.read().split("\n")
    file.close()

    return follower_list


def add_username(username, name = "usernames_to_check"):
    path = get_parsed_cwd()+ "\ "[:-1] + name
    file = open(path,"a+")
    file.write("\n" + username)
    file.close()

if __name__ == '__main__':
    add_username("deneme")


