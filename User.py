from aiohttp.web_fileresponse import content_type

import file_handeling as fh

Content = {}
content_1 = {}

def lines(number):
    for i in range(number):
        print("-", end="")
    print()

def choice_yes_n_no(user_choice):
    while True:
        if user_choice.lower() in ["yes", "y", "ye"]:
            return
        elif user_choice.lower() in ["no", "n"]:
            break
        else:
            print("Invalid input. Please try again.\nPlease enter \"yes\" or \"no\".")

def search_content_by_name(content_title):
    fh.reader(Content, "comments.csv")

    for content_id,data in Content.items():
        title = data[0]
        comment = data[1]

        if content_id[0] == "m":
            content_type = "movie"
        elif content_id[0] == "t":
            content_type  = "tv-show"
        else:
            content_type = "anime"

        if content_title.lower() == title.lower():
            print(f"Name of the {content_type.capitalize()} is {title.capitalize()}.")
            print(f"Comments ----->")
            lines(20)
            print(f"{comment}")

# search_content_by_name("The Witch and the Beast")


def write_comment(content):
    while True:
        new_comment = ""
        content_name = input(f"Enter the name of the {content} you want to comment: ")
        fh.reader(content, "comments.csv")
        for content_id,data in Content.items():
            title = data[0]
            comment = data[1]
            if title.lower() == content_name.lower():
                if len(comment) == 0:
                    while True:
                        new_comment = input(f"Enter the new comment for {title.capitalize()}: ")
                        if len(new_comment) > 0:
                            break
                        else:
                            while True:
                                user_choice = input(f"You're not entering a comment for {title.capitalize()} (yes/no): ")
                                if user_choice.lower() in ["yes", "y", "ye"]:
                                    return
                                elif user_choice.lower() in ["no", "n"]:
                                    break
                                else:
                                    print("Invalid input. Please try again.\nPlease enter \"yes\" or \"no\".")
                else:
                    print(f"The {content.capitalize()}, {title.capitalize()} already has a comment.")
                    while True:
                        user_choice = input("Do you want to add new one or replace existing one?\n01. Add a new one\n2. Replace existing one\n3. Exit\n ------------------->  ")
                        if user_choice.lower() in ["add new", "add", "add a new one", "add a new", "01", "1"]:
                            return
                        elif user_choice.lower() in ["replace existing", "replace", "replace existing one","2","02"]:
                            break
                        elif user_choice.lower() in ["exit", "3", "03"]:
                            print("hi")
                        else:
                            print("Invalid input. Please try again.\nPlease enter \"01\" or \"2\" or \"03\".")



        comment = input("Enter a comment: ")



def rewrite_csv():
    fh.reader(Content, "AnimeShows.csv")
    i = 1
    for content_id,data in Content.items():
        new_content_id = f"a{i}"
        title = content_id

        i = i + 1
        print(new_content_id,title,data)
        content_1[new_content_id] = [title] + data[1:]

    for content_id,data in content_1.items():
        print(content_id,data)

    fh.writer(content_1, "AnimeShows_1.csv")


rewrite_csv()


