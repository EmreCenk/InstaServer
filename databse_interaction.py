
# for now I will be using a text file to emulate a database. Hopefully I won't need to create an actual remote databse
# in the future.

def parse_usernames(file_path, separator_character):
    file = open(file_path, "r")
    text = file.read().split(separator_character)
    file.close()

    return text

