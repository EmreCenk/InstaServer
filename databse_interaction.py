
# for now I will be using a text file to emulate a database. Hopefully I won't need to create an actual remote databse
# in the future.

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